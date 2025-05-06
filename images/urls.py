from django.urls import path, include
from images import views

urlpatterns = [
    path("", views.images_list),
    path("<int:pk>", views.image_detail),
]
