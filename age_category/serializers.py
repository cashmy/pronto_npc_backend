from rest_framework import serializers
from .models import AgeCategory


class AgeCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the AgeCategory model.
    Handles create, retrieve, update operations for age categories.
    """

    class Meta:
        model = AgeCategory
        fields = ["id", "age_category_name", "description", "created_at", "updated_at"]
        extra_kwargs = {
            "description": {"required": False, "allow_blank": True, "allow_null": True}
        }
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


# Serializer for the dropdown options in the frontend
class AgeCategoryOptionSerializer(serializers.ModelSerializer):
    """
    A simplified serializer for AgeCategory, providing 'id' and 'value' (name)
    primarily for use in frontend dropdowns or select lists.
    """

    value = serializers.CharField(
        source="age_category_name", help_text="The display name of the age category."
    )

    class Meta:
        model = AgeCategory
        fields = ["id", "value"]
        help_texts = {
            "id": "The unique identifier for the age category.",
        }
