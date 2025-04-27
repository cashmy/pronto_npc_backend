from rest_framework import serializers
from .models import Archetype


class ArchetypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archetype
        fields = [
            "id",
            "name",
            "description",
            "notes",
            "expansion",
            "related_archetypes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        return Archetype.objects.create(**validated_data)
