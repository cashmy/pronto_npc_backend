from django.urls import path
from table_group import views

urlpatterns = [
    path("", views.table_group_list, name="table_group_list"),
    path("<int:pk>/", views.table_group_detail, name="table_group_detail"),
]
