from django.urls import path
from system import views

urlpatterns = [
    path("", views.system_list, name="system_list"),
    path("<int:pk>/", views.system_detail, name="system_detail"),
]
