from django.urls import path
from character_group import views

urlpatterns = [
    path("", views.character_group_list, name="character_group_list"),
    path("<int:pk>/", views.character_group_detail, name="character_group_detail"),
]
