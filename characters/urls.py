from django.urls import path
from characters import views

urlpatterns = [
    path("", views.character_list, name="character_list"),
    path("<int:pk>/", views.character_detail, name="character_detail"),
]
