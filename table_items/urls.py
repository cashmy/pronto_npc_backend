from django.urls import path
from table_items import views

urlpatterns = [
    path("", views.table_item_list, name="table_item_list"),
    path("<int:pk>/", views.table_item_detail, name="table_item_detail"),
]
