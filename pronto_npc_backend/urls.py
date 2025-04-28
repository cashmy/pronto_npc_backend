from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static helper

urlpatterns = [
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
    # path("api/users/", include("users.urls")),
    # path("api/profiles/", include("profiles.urls")),
    # path("api/subscriptions/", include("subscriptions.urls")),
    path("api/age_category/", include("age_category.urls")),
]

# Add this block to serve media files during development (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
