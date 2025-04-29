# users/views.py

from dj_rest_auth.registration.views import (
    RegisterView,
    SocialLoginView,
    ResendEmailVerificationView,
)
from dj_rest_auth.views import LoginView
from users.serializers import CustomRegisterSerializer
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from users.models import OneTimePassword
from django.core.mail import send_mail
from datetime import timedelta
from django.utils import timezone

from users.serializers import OTPVerifySerializer


class OTPVerifyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = OTPVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp_input = serializer.validated_data["otp"]
        otp_obj = OneTimePassword.objects.filter(
            user=request.user, code=otp_input
        ).first()
        if not otp_obj or otp_obj.is_expired():
            return Response({"detail": "Invalid or expired OTP"}, status=400)

        # OTP is valid
        otp_obj.delete()
        request.user.profile.is_2fa_verified = True
        request.user.profile.save()

        return Response({"detail": "2FA verification complete"})


# ----- Standard Registration -----


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    def get_response_data(self, user):
        # Issue JWT tokens directly after successful registration
        refresh = RefreshToken.for_user(user)
        return {
            "user_id": user.id,
            "email": user.email,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }


# ----- Standard Login -----


class CustomLoginView(LoginView):
    """
    Optional: Override if you want to trigger 2FA email OTP after login.
    """

    def get_response(self):
        response = super().get_response()

        # After successful login, send 2FA OTP email
        if self.request.user and not self.request.user.is_superuser:
            send_login_otp(self.request.user)

        return response


# ----- Social Logins -----


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


# ----- Resend Email Verification -----


class CustomResendEmailVerificationView(ResendEmailVerificationView):
    """
    This view resends the email verification link if user didn't get it originally.
    """


# ----- 2FA OTP Verification -----


class OTPVerifyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        otp_input = request.data.get("otp")
        otp_obj = OneTimePassword.objects.filter(
            user=request.user, code=otp_input
        ).first()
        if not otp_obj or otp_obj.is_expired():
            return Response({"detail": "Invalid or expired OTP"}, status=400)

        # OTP is valid
        otp_obj.delete()
        request.user.profile.is_2fa_verified = True
        request.user.profile.save()

        return Response({"detail": "2FA verification complete"})


# ----- Soft Deactivate (Account Deletion) -----


class DeactivateMeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        user.is_active = False
        user.save()
        return Response({"detail": "Your account has been deactivated"})


# ----- Utility function to send OTP -----


def send_login_otp(user):
    """
    Sends an email with OTP code for Two-Factor Authentication (2FA).
    """
    otp_code = OneTimePassword.generate_otp()
    OneTimePassword.objects.create(user=user, code=otp_code)
    send_mail(
        "Your Login OTP Code",
        f"Use this OTP code to complete your login: {otp_code}",
        "no-reply@yourdomain.com",
        [user.email],
        fail_silently=False,
    )
