from django.urls import path
from npc_system_professions import views

urlpatterns = [
    path("", views.npc_system_professions_list, name="npc_system_professions_list"),
    path(
        "<int:pk>",
        views.npc_system_professions_detail,
        name="npc_system_profession_detail",
    ),
    path(
        "options/<int:npc_system_pk>/",
        views.npc_system_profession_options,
        name="npc_system_profession_options",
    ),
]
