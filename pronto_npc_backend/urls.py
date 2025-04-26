from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static helper

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/npc_system/", include("npc_system.urls")),
    path("api/images/", include("images.urls")),
]

# Add this block to serve media files during development (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
