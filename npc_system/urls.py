from django.urls import path
from npc_system import views

urlpatterns = [
    path("", views.npc_system_list, name="npc_system_list"),
    path("<int:pk>/", views.npc_system_detail, name="npc_system_detail"),
]
