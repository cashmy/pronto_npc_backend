from django.urls import path
from table_items import views

urlpatterns = [
    path("", views.table_item_list, name="table_item_list"),
    path("<int:pk>", views.table_item_detail, name="table_item_detail"),
    path(
        "table_header/<int:table_header>",
        views.table_items_list_by_table_header,
        name="table_items_list_by_table_header",
    ),
]
