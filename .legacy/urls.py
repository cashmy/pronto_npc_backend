from django.urls import path
from npc_system_races import views

urlpatterns = [
    path("", views.npc_system_races_list, name="npc_system_races_list"),
    path("<int:pk>/", views.npc_system_races_detail, name="npc_system_race_detail"),
    path(
        "options/<int:npc_system_pk>/",
        views.npc_system_race_options,
        name="npc_system_race_options",
    ),
    path(
        "random-race/<int:npc_system_pk>/",
        views.get_random_npc_system_race,
        name="get_ra ndom_npc_system_race",
    ),
]
