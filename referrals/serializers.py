# referrals/serializers.py

from rest_framework import serializers
from referrals.models import Referral


class ReferralSerializer(serializers.ModelSerializer):
    referral_link = serializers.SerializerMethodField()

    class Meta:
        model = Referral
        fields = ("code", "referral_link", "created_at")

    def get_referral_link(self, obj):
        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(f"/register?ref={obj.code}")
        return f"/register?ref={obj.code}"
