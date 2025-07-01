from rest_framework import serializers

from .models import Genre


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer for the Genre model.

    This serializer handles the serialization and deserialization of Genre
    instances, exposing all fields for standard CRUD operations.

    Attributes:
        id (int): The unique identifier for the genre.
        name (str): The name of the genre.
        description (str): A detailed description of the genre.
        notes (str): Optional internal notes about the genre.
        icon (File): An icon representing the genre.
        created_at (datetime): The timestamp when the genre was created.
        updated_at (datetime): The timestamp when the genre was last updated.
    """

    class Meta:
        """Meta options for the GenreSerializer."""

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
        """
        Create and return a new `Genre` instance, given the validated data.

        Args:
            validated_data (dict): The data to create the genre with.

        Returns:
            Genre: The newly created genre instance.
        """
        return Genre.objects.create(**validated_data)


# Serializer for the dropdown options in the frontend
class GenreOptionSerializer(serializers.ModelSerializer):
    """
    A simplified serializer for providing genre options.

    This serializer is designed for use in frontend components like dropdowns,
    providing a minimal set of data (`id`, `value`, `icon`) for selection.
    The `name` field is aliased to `value` for compatibility with common
    frontend libraries.

    Attributes:
        id (int): The unique identifier for the genre.
        value (str): The name of the genre, aliased from the 'name' field.
        icon (File): An icon representing the genre.
    """

    value = serializers.CharField(source="name")

    class Meta:
        """Meta options for the GenreOptionSerializer."""

        model = Genre
        fields = ["id", "value", "icon"]
