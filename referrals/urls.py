# referrals/urls.py

from django.urls import path
from referrals.views import MyReferralLinkView

urlpatterns = [
    path("my-invite/", MyReferralLinkView.as_view(), name="my_referral_link"),
]
