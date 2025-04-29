from rest_framework import serializers
from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    referred_by_email = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ("avatar", "bio", "date_of_birth", "referred_by_email")

    def get_referred_by_email(self, obj):
        return obj.referred_by.email if obj.referred_by else None
