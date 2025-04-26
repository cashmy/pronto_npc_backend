from django.urls import path
from character_sub_group import views

urlpatterns = [
    path("", views.character_sub_group_list, name="character_sub_group_list"),
    path(
        "<int:pk>/", views.character_sub_group_detail, name="character_sub_group_detail"
    ),
]
