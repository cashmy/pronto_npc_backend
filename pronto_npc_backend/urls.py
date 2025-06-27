from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static helper
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenVerifyView

# from dj_rest_auth.views import TokenRefreshView
from users.views import CookieTokenRefreshView, CustomLoginView

urlpatterns = [
    # JWT-aware auth
    path("auth/login/", CustomLoginView.as_view(), name="rest_login"),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    # Use dj_rest_auth's TokenRefreshView to read refresh token from cookie
    path(
        "auth/token/refresh/", CookieTokenRefreshView.as_view(), name="token_refresh"
    ),  # Changed
    path("auth/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # Admin and app routes
    path("admin/", admin.site.urls),
    # Group all API endpoints under the /api/ prefix
    path("api/", include("pronto_npc_backend.api_urls")),
]

# Add this block to serve media files during development (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
