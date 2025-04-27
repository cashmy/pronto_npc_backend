from django.urls import path
from character_images import views

urlpatterns = [
    path("", views.character_image_list, name="character_image_list"),
    path("<int:pk>/", views.character_image_detail, name="character_image_detail"),
]
