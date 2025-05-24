# users/views.py

from dj_rest_auth.registration.views import (
    RegisterView,
    SocialLoginView,
    ResendEmailVerificationView,
)
from dj_rest_auth.views import LoginView, LogoutView as DjRestAuthLogoutView
from dj_rest_auth.app_settings import api_settings as dj_rest_auth_settings
from dj_rest_auth.jwt_auth import unset_jwt_cookies
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, serializers

# Import necessary classes for the custom refresh view
from rest_framework_simplejwt.views import (
    TokenRefreshView as SimpleJWTTokenRefreshView,
)
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer as SimpleJWTTokenRefreshSerializer,
)

from django.core.mail import send_mail
from django.conf import settings as django_settings
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import timedelta

from users.models import OneTimePassword
from users.serializers import CustomRegisterSerializer


from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from users.serializers import (
    OTPVerifySerializer,
    CustomUsernameOrEmailLoginSerializer,
    CombinedUserDataSerializer,
)

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
            "accessToken": str(refresh.access_token),
            "refreshToken": str(refresh),
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
            "accessToken": access_token,
            "refreshToken": refresh_token,  # Leave for now, But remove for production
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
        # new_refresh_token = validated_data.get(
        #     "refresh"  # This will be None if ROTATE_REFRESH_TOKENS is False in settings.
        #     # If ROTATE_REFRESH_TOKENS is True, a new refresh token would be present here.
        # )

        set_jwt_cookies(response, new_access_token, refresh_token_from_cookie)

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


# ----- Custom Logout -----


class CustomLogoutView(DjRestAuthLogoutView):
    """
    Custom LogoutView to ensure the refresh token from the HttpOnly cookie
    is blacklisted and then all JWT cookies are cleared.
    """

    permission_classes = [
        permissions.IsAuthenticated
    ]  # Ensure user is authenticated to logout

    def logout(self, request):
        response = Response(
            {"detail": _("Successfully logged out.")},
            status=status.HTTP_200_OK,
        )

        # 1. Blacklist the refresh token from the cookie
        refresh_token_name = dj_rest_auth_settings.JWT_AUTH_REFRESH_COOKIE
        refresh_token_from_cookie = request.COOKIES.get(refresh_token_name)

        if refresh_token_from_cookie:
            # Check if the blacklist app is installed
            if (
                "rest_framework_simplejwt.token_blacklist"
                in django_settings.INSTALLED_APPS
            ):
                try:
                    token = RefreshToken(refresh_token_from_cookie)
                    token.blacklist()
                except TokenError:
                    # Token might be already blacklisted or invalid (e.g., expired)
                    pass
                except Exception:
                    # Log this error, but don't fail the logout.
                    # Consider adding proper logging here.
                    # For example: logger.error("Error blacklisting token from cookie", exc_info=True)
                    pass

        # 2. Unset JWT cookies (access and refresh)
        # unset_jwt_cookies modifies the response passed to it.
        if dj_rest_auth_settings.USE_JWT:
            unset_jwt_cookies(response)

        # 3. Perform Django's session logout if session login is enabled
        # (though with USE_JWT=True, SESSION_LOGIN is typically False by default in dj-rest-auth)
        if dj_rest_auth_settings.SESSION_LOGIN:
            from django.contrib.auth import logout as django_logout

            django_logout(request)

        # 4. Send the user_logged_out signal (copied from dj_rest_auth behavior)
        if hasattr(request, "user") and request.user.is_authenticated:
            from django.contrib.auth.signals import user_logged_out

            user_logged_out.send(
                sender=request.user.__class__, request=request, user=request.user
            )

        return response

    def post(self, request, *args, **kwargs):
        # The `logout` method in DjRestAuthLogoutView is called by `post`
        # We've overridden `logout`, so this will call our custom logic.
        return self.logout(request)


# ----- Combined User Data -----


class CombinedUserDataView(APIView):
    """
    Provides combined user data including profile, active subscription,
    and usage tracking information. Intended for use after login to
    populate frontend state.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = CombinedUserDataSerializer(user, context={"request": request})
        return Response(serializer.data)
