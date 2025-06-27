# referrals/serializers.py

from rest_framework import serializers
from referrals.models import Referral
from profiles.models import Profile  # Import Profile model


class ReferralSerializer(serializers.ModelSerializer):
    referral_link = serializers.SerializerMethodField()

    class Meta:
        model = Referral
        fields = ("code", "referral_link", "created_at", "referred_user_count")

    def get_referral_link(self, obj):
        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(f"/register?ref={obj.code}")
        return f"/register?ref={obj.code}"


class ReferredUserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for listing users referred by the current user.
    Provides email, first_name, last_name, and avatar.
    """

    email = serializers.EmailField(source="user.email", read_only=True)
    first_name = serializers.CharField(
        source="user.first_name", read_only=True, allow_blank=True, allow_null=True
    )
    last_name = serializers.CharField(
        source="user.last_name", read_only=True, allow_blank=True, allow_null=True
    )

    # 'avatar' is a direct field from the Profile model
    class Meta:
        model = Profile
        fields = ("email", "first_name", "last_name", "avatar")
