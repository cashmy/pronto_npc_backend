from rest_framework import serializers
from usage_tracking.models import UsageTracking


class UsageTrackingSerializer(serializers.ModelSerializer):
    """
    Serializer for tracking user usage metrics.
    """

    user_username = serializers.CharField(source="user.username", read_only=True)
    user_email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = UsageTracking
        fields = (
            "id",
            "user",
            "user_email",
            "user_username",
            "npc_systems_generated_count",
            "characters_generated_count",
            "custom_generators_created_count",
            "ai_interfaced_characters_count",
            "ai_image_generated_characters_count",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "user",
            "user_email",
            "user_username",
            "created_at",
            "updated_at",
        )
