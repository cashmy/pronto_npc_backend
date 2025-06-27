from rest_framework import serializers
from .models import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = [
            "id",
            "name",
            "description",
            "notes",
            "icon",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)


# Serializer for the dropdown options in the frontend
class GenreOptionSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source="name")

    class Meta:
        model = Genre
        fields = ["id", "value", "icon"]
