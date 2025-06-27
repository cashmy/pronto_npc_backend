from django.urls import path
from table_header import views

urlpatterns = [
    path("", views.table_header_list, name="table_header_list"),
    path("<int:pk>", views.table_header_detail, name="table_header_detail"),
    path(
        "system/<int:npc_system_id>",
        views.table_header_list_by_system,
        name="table_header_list_by_system",
    ),
    path(
        "system/<int:npc_system_id>/<int:table_group_id>",
        views.table_header_list_by_system_and_group,
        name="table_header_list_by_system_and_group",
    ),
]
