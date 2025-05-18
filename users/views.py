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
from rest_framework import status, permissions, serializers
from users.models import OneTimePassword
from django.core.mail import send_mail
from datetime import timedelta
from django.utils import timezone

# Import necessary classes for the custom refresh view
from rest_framework_simplejwt.views import (
    TokenRefreshView as SimpleJWTTokenRefreshView,
)
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer as SimpleJWTTokenRefreshSerializer,
)

from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from users.serializers import OTPVerifySerializer, CustomUsernameOrEmailLoginSerializer

# Import for dj-rest-auth settings and cookie utilities
from dj_rest_auth.app_settings import api_settings as dj_rest_auth_settings
from dj_rest_auth.jwt_auth import set_jwt_cookies

from rest_framework.permissions import IsAuthenticated


class DebugUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response(
            {
                "raw_user": str(user),
                "type": str(type(user)),
                "is_authenticated": getattr(user, "is_authenticated", False),
                "user_id": getattr(user, "id", None),
                "username": getattr(user, "username", None),
                "email": getattr(user, "email", None),
                "first_name": getattr(user, "first_name", None),
                "last_name": getattr(user, "last_name", None),
                "is_staff": getattr(user, "is_staff", None),
                "is_superuser": getattr(user, "is_superuser", None),
                "is_active": getattr(user, "is_active", None),
                "date_joined": getattr(user, "date_joined", None),
                "last_login": getattr(user, "last_login", None),
                "is_email_verified": getattr(user, "is_email_verified", None),
            }
        )


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
    serializer_class = CustomUsernameOrEmailLoginSerializer

    """
    Optional: Override if you want to trigger 2FA email OTP after login.
    """

    def get_response(self):
        user = (
            self.user
        )  # self.user is set by the parent LoginView's process_login method
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        response_data = {
            "user_id": user.id,
            "email": user.email,
            "access": access_token,
            "refresh": refresh_token,  # Leave for now, But remove for production
        }
        response = Response(response_data, status=status.HTTP_200_OK)
        # Use dj_rest_auth's utility to set the HttpOnly refresh token cookie
        set_jwt_cookies(response, access_token, refresh_token)
        return response


class CookieTokenRefreshView(SimpleJWTTokenRefreshView):
    """
    Custom TokenRefreshView that uses dj_rest_auth's TokenRefreshSerializer
    to read the refresh token from an HttpOnly cookie.
    """

    serializer_class = SimpleJWTTokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        refresh_token_name = dj_rest_auth_settings.JWT_AUTH_REFRESH_COOKIE
        refresh_token_from_cookie = request.COOKIES.get(refresh_token_name)
        data = {}
        # Prioritize token from cookie if available
        if refresh_token_from_cookie:
            data["refresh"] = refresh_token_from_cookie
        else:
            # Fallback to request body if cookie not present or empty.
            # This allows clients that might not send cookies (e.g. testing, non-browser)
            # or if the cookie somehow wasn't set/sent.
            # If you want to strictly enforce cookie-only, you could raise an error here
            # if refresh_token_from_cookie is None.
            if "refresh" not in request.data:
                return Response(
                    {"detail": "Refresh token not found in cookie or request body."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            data["refresh"] = request.data.get("refresh")

        serializer = self.get_serializer(data=data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            # Convert TokenError to InvalidToken as expected by DRF for consistent error handling
            raise InvalidToken(e.args[0])
        except (
            serializers.ValidationError
        ) as e:  # Catch validation errors from the serializer
            raise InvalidToken(e.detail)  # Re-raise as InvalidToken for consistency

        validated_data = serializer.validated_data
        response = Response(validated_data, status=status.HTTP_200_OK)

        # Use dj-rest-auth's utility to set JWT cookies in the response.
        # This will handle setting the new refresh token (due to rotation)
        # and potentially an access token cookie if JWT_AUTH_COOKIE were configured (it's None in your settings).
        new_access_token = validated_data.get("access")
        new_refresh_token = validated_data.get(
            "refresh"
        )  # Will be present due to ROTATE_REFRESH_TOKENS=True

        set_jwt_cookies(response, new_access_token, new_refresh_token)

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
