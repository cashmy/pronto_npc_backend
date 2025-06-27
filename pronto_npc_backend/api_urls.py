from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

# This file groups all API-specific endpoints under a common namespace.
urlpatterns = [
    # OpenAPI Schema and UI paths are part of the API, so they belong here.
    # We are explicitly setting the permission and authentication classes here
    # to bypass any potential issues with settings loading and ensure public access.
    path(
        "schema/",
        SpectacularAPIView.as_view(authentication_classes=[], permission_classes=[]),
        name="api-schema",
    ),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(
            url_name="api-schema", authentication_classes=[], permission_classes=[]
        ),
        name="api-swagger-ui",
    ),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(
            url_name="api-schema", authentication_classes=[], permission_classes=[]
        ),
        name="api-redoc",
    ),
    # Application-specific API routes
    path("npc_system/", include("npc_system.urls")),
    path("images/", include("images.urls")),
    path("character_group/", include("character_group.urls")),
    path("character_sub_group/", include("character_sub_group.urls")),
    path("archetype/", include("archetype.urls")),
    path("genre/", include("genre.urls")),
    path("characters/", include("characters.urls")),
    path("character_images/", include("character_images.urls")),
    path("npc_system_races/", include("npc_system_races.urls")),
    path("npc_system_rpg_classes/", include("npc_system_rpg_classes.urls")),
    path("npc_system_professions/", include("npc_system_professions.urls")),
    path("table_group/", include("table_group.urls")),
    path("table_header/", include("table_header.urls")),
    path("table_items/", include("table_items.urls")),
    path("users/", include("users.urls")),
    path("profiles/", include("profiles.urls")),
    path("subscriptions/", include("subscriptions.urls")),
    path("age_category/", include("age_category.urls")),
    path("referrals/", include("referrals.urls")),
    path("usage_tracking/", include("usage_tracking.urls")),
]
