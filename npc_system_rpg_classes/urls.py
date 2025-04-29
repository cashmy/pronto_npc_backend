from django.urls import path
from npc_system_rpg_classes import views

urlpatterns = [
    path("", views.npc_system_rpg_classes_list, name="npc_system_rpg_classes_list"),
    path(
        "<int:pk>/", views.npc_system_rpg_classes_detail, name="npc_system_race_detail"
    ),
    path(
        "options/",
        views.npc_system_rpg_class_options,
        name="npc_system_rpg_class_options",
    ),
]
