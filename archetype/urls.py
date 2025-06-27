from django.urls import path
from archetype import views

urlpatterns = [
    path("", views.archetype_list, name="archetype_list"),
    path(
        "by_expansion/",
        views.archetype_list_by_expansion,
        name="archetype_list_by_expansion",
    ),
    path("<int:pk>", views.archetype_detail, name="archetype_detail"),
]
