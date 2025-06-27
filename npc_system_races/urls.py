from django.urls import include, path
from rest_framework.routers import DefaultRouter

from npc_system_races import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r"", views.NpcSystemRaceViewSet, basename="npc_system_race")

urlpatterns = [
    path("", include(router.urls)),
]
