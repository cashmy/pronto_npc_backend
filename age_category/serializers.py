from rest_framework import serializers
from .models import AgeCategory


class AgeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeCategory
        fields = ["id", "age_category_name", "description", "created_at", "updated_at"]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


# Serializer for the dropdown options in the frontend
class AgeCategoryOptionSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source="age_category_name")

    class Meta:
        model = AgeCategory
        fields = ["id", "value"]
