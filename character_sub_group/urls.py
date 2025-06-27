from django.urls import path
from character_sub_group import views

urlpatterns = [
    path("", views.character_sub_group_list, name="character_sub_group_list"),
    path(
        "<int:pk>", views.character_sub_group_detail, name="character_sub_group_detail"
    ),
    path(
        "system/<int:npc_system_id>",
        views.character_sub_group_list_by_system,
        name="character_sub_group_list_by_system",
    ),
    path(
        "system/<int:npc_system_id>/<int:character_group_id>",
        views.character_sub_group_list_by_system_and_group,
        name="character_sub_group_list_by_system_and_group",
    ),
]
