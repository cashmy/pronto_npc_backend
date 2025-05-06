from rest_framework import serializers
from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    # Display user's email and username for context, read-only.
    user_email = serializers.EmailField(source="user.email", read_only=True)
    user_username = serializers.CharField(source="user.username", read_only=True)
    user_first_name = serializers.CharField(source="user.first_name", read_only=True)
    user_last_name = serializers.CharField(source="user.last_name", read_only=True)

    class Meta:
        model = Profile
        fields = (
            "id",  # The ID of the Profile record itself
            "user",  # The ID of the associated User (read-only in most contexts)
            "user_email",
            "user_username",
            "user_first_name",
            "user_last_name",
            "avatar",
            "bio",
            "date_of_birth",
            "referred_by_email",  # Direct model field
            "theme",
            "discord_id",
            "location",
        )
        read_only_fields = (
            "id",
            "user",
            "user_email",
            "user_username",
            "user_first_name",
            "user_last_name",
            "referred_by_email",  # Assuming this is set at creation and not typically updated by user directly
        )
        # If 'referred_by_email' should be updatable via profile edit, remove it from read_only_fields.
