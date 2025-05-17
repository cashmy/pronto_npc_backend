from django.urls import path
from npc_system_rpg_classes import views

urlpatterns = [
    path("", views.npc_system_rpg_classes_list, name="npc_system_rpg_classes_list"),
    path(
        "<int:pk>/", views.npc_system_rpg_classes_detail, name="npc_system_race_detail"
    ),
    path(
        "options/<int:npc_system_pk>/",
        views.npc_system_rpg_class_options,
        name="npc_system_rpg_class_options",
    ),
    path(
        "random-class/<int:npc_system_pk>/",
        views.get_random_npc_system_rpg_class,
        name="get_ra ndom_npc_system_rpg_class",
    ),
]
