from django.urls import path
from archetype import views

urlpatterns = [
    path("", views.archetype_list, name="archetype_list"),
    path("<int:pk>/", views.archetype_detail, name="archetype_detail"),
]
