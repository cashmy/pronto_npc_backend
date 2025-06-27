from django.urls import path
from profiles import views  # Import views module


urlpatterns = [
    path("me/", views.profile_me, name="profile_me"),
    # The following are typically for admin use or specific scenarios
    path("", views.profile_list, name="profile_list_admin"),
    path("<int:pk>", views.profile_detail_by_pk, name="profile_detail_admin"),
]
