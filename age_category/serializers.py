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
