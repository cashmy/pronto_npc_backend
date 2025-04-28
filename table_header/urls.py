from django.urls import path
from table_header import views

urlpatterns = [
    path("", views.table_header_list, name="table_header_list"),
    path("<int:pk>/", views.table_header_detail, name="table_header_detail"),
]
