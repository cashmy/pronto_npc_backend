from rest_framework import serializers

from .models import Archetype


class ArchetypeSerializer(serializers.ModelSerializer):
    """Serializer for the Archetype model.

    This serializer handles the conversion of Archetype model instances to and from
    JSON format. It includes all fields from the Archetype model and sets specific
    fields as read-only.

    Attributes:
        Meta (class): A nested class that defines metadata options for the serializer,
                      such as the model to use and the fields to include.
    """

    class Meta:
        """Metadata options for the ArchetypeSerializer."""

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
        """Create and return a new `Archetype` instance, given the validated data.

        Args:
            validated_data (dict): A dictionary of validated data for creating a new archetype.

        Returns:
            Archetype: The newly created Archetype instance.
        """
        return Archetype.objects.create(**validated_data)
