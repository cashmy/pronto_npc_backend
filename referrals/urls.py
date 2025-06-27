# referrals/urls.py

from django.urls import path
from . import views  # Use relative import for views


urlpatterns = [
    path("my-invite/", views.my_referral_link, name="my_referral_link"),
    path("referred-users/", views.list_referred_users, name="list_referred_users"),
]
