from django.urls import path
from genre import views

urlpatterns = [
    path("", views.genre_list, name="genre_list"),
    path("<int:pk>", views.genre_detail, name="genre_detail"),
    path("options/", views.genre_options, name="genre_options"),
]
