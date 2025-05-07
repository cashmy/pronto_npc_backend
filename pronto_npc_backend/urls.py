from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static helper
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from users.views import CustomLoginView

urlpatterns = [
    # JWT-aware auth
    path("auth/login/", CustomLoginView.as_view(), name="rest_login"),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # Admin and app routes
    path("admin/", admin.site.urls),
    path("api/npc_system/", include("npc_system.urls")),
    path("api/images/", include("images.urls")),
    path("api/character_group/", include("character_group.urls")),
    path("api/character_sub_group/", include("character_sub_group.urls")),
    path("api/archetype/", include("archetype.urls")),
    path("api/genre/", include("genre.urls")),
    path("api/characters/", include("characters.urls")),
    path("api/character_images/", include("character_images.urls")),
    path("api/npc_system_races/", include("npc_system_races.urls")),
    path("api/npc_system_rpg_classes/", include("npc_system_rpg_classes.urls")),
    path("api/npc_system_professions/", include("npc_system_professions.urls")),
    path("api/table_group/", include("table_group.urls")),
    path("api/table_header/", include("table_header.urls")),
    path("api/table_items/", include("table_items.urls")),
    path("api/users/", include("users.urls")),
    path("api/profiles/", include("profiles.urls")),
    path("api/subscriptions/", include("subscriptions.urls")),
    path("api/age_category/", include("age_category.urls")),
    path("api/referrals/", include("referrals.urls")),
    path("api/usage_tracking/", include("usage_tracking.urls")),
]

# Add this block to serve media files during development (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
