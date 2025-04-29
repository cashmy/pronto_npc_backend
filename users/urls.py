# users/urls.py

from django.urls import path
from users.views import (
    CustomRegisterView,
    CustomLoginView,
    GoogleLogin,
    FacebookLogin,
    CustomResendEmailVerificationView,
    OTPVerifyView,
    DeactivateMeView,
)
from dj_rest_auth.views import (
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from dj_rest_auth.registration.views import VerifyEmailView

urlpatterns = [
    # Authentication
    path("login/", CustomLoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    # Registration
    path("registration/", CustomRegisterView.as_view(), name="rest_register"),
    path(
        "registration/verify-email/",
        VerifyEmailView.as_view(),
        name="rest_verify_email",
    ),
    path(
        "registration/resend-email/",
        CustomResendEmailVerificationView.as_view(),
        name="rest_resend_email",
    ),
    # Password Management
    path("password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path(
        "password/reset/confirm/",
        PasswordResetConfirmView.as_view(),
        name="rest_password_reset_confirm",
    ),
    path("password/change/", PasswordChangeView.as_view(), name="rest_password_change"),
    # Social OAuth Logins
    path("social/google/", GoogleLogin.as_view(), name="google_login"),
    path("social/facebook/", FacebookLogin.as_view(), name="facebook_login"),
    # Two-Factor Authentication
    path("otp/verify/", OTPVerifyView.as_view(), name="otp_verify"),
    # Account Deactivation (Soft Delete)
    path("deactivate/", DeactivateMeView.as_view(), name="deactivate_account"),
]
