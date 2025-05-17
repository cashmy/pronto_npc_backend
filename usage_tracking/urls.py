from django.urls import path
from usage_tracking import views


urlpatterns = [
    path("me/", views.usage_tracking_me, name="usage_tracking_me"),
    # The following are typically for admin use or specific scenarios
    path("", views.usage_tracking_list, name="usage_tracking_list_admin"),
    path(
        "<int:pk>",
        views.usage_tracking_detail_by_pk,
        name="usage_tracking_detail_admin",
    ),
]
