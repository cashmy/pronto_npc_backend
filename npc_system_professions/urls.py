from django.urls import include, path
from rest_framework.routers import DefaultRouter

from npc_system_professions import views

# Create a router and register our ViewSet with it.
router = DefaultRouter()
router.register(r"", views.NpcSystemProfessionViewSet, basename="npc_system_profession")

urlpatterns = [
    path("", include(router.urls)),
]
