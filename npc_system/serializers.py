from rest_framework import serializers
from .models import NpcSystem


class NpcSystemSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(
        source="genre.name", read_only=True
    )  # Display the genre name instead of the ID

    class Meta:
        model = NpcSystem
        fields = [
            "id",
            "system_name",
            "description",
            "genre",
            "standard_app_dsp",
            "is_global",
            "owner",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        """
        Automatically set the owner as the request user for custom systems.
        """
        request = self.context.get("request")
        if request and not validated_data.get("is_global", False):
            validated_data["owner"] = request.user
        return super().create(validated_data)

    def validate_is_global(self, value):
        if value and not self.context["request"].user.is_staff:
            raise serializers.ValidationError("Only admins can create global systems.")
        return value
