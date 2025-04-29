# referrals/views.py

from rest_framework import generics, permissions
from referrals.models import Referral
from referrals.serializers import ReferralSerializer


class MyReferralLinkView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReferralSerializer

    def get_object(self):
        referral, created = Referral.objects.get_or_create(
            referred_by=self.request.user
        )
        return referral
