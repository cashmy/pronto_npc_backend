from rest_framework import serializers
from .models import AgeCategory


class AgeCategorySerializer(serializers.ModelSerializer):
    """Serializes AgeCategory data for API endpoints.

    This serializer handles the representation of AgeCategory objects for
    standard CRUD operations.

    Attributes:
        id (int): The unique primary key for the age category. Read-only.
        age_category_name (str): The name of the age category (e.g., "Adult").
        description (str): An optional, detailed description.
        created_at (datetime): Timestamp of creation. Read-only.
        updated_at (datetime): Timestamp of last update. Read-only.
    """

    class Meta:
        """Sets the model and fields for the serializer."""
        model = AgeCategory
        fields = ["id", "age_category_name", "description", "created_at", "updated_at"]
        extra_kwargs = {
            "description": {"required": False, "allow_blank": True, "allow_null": True}
        }
        read_only_fields = ["id", "created_at", "updated_at"]


class AgeCategoryOptionSerializer(serializers.ModelSerializer):
    """Provides a simplified representation of age categories for dropdowns.

    This serializer exposes only the fields necessary for populating a
    select/option list in a frontend application, making it lightweight.

    Attributes:
        id (int): The unique identifier for the age category.
        value (str): The display name of the age category.
    """

    value = serializers.CharField(source="age_category_name")

    class Meta:
        """Sets the model and fields for the serializer."""
        model = AgeCategory
        fields = ["id", "value"]
