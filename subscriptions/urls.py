# subscriptions/urls.py

from django.urls import path
from . import views  # Use relative import for views

urlpatterns = [
    path("me/", views.subscription_me, name="subscription_me"),
    path("upgrade/", views.subscription_upgrade, name="subscription_upgrade"),
    path(
        "me/deactivate/",
        views.subscription_deactivate_me,
        name="subscription_deactivate_me",
    ),
    path(
        "me/reactivate/",
        views.subscription_reactivate_me,
        name="subscription_reactivate_me",
    ),
    path(
        "<int:pk>/admin-update/",
        views.subscription_admin_update,
        name="subscription_admin_update",
    ),
]
