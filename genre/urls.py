from django.urls import path
from genre import views

urlpatterns = [
    path("", views.genre_list, name="genre_list"),
    path("<int:pk>", views.genre_detail, name="genre_detail"),
    path("options/", views.genre_options, name="genre_options"),
    path(
        "random-genre/",
        views.get_random_genre,
        name="get_random_genre",
    ),
]
