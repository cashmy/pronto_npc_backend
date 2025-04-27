from rest_framework import serializers
from .models import CharacterImage
from images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Image model to include all fields.
    """

    class Meta:
        model = Image
        fields = "__all__"  # Include all fields from the Image model


class CharacterImageSerializer(serializers.ModelSerializer):
    """
    Serializer for the CharacterImage model.
    Includes the full name and race of the character and all fields from the Image model.
    """

    character_full_name = serializers.SerializerMethodField()
    character_race = serializers.CharField(source="character.race", read_only=True)
    image = ImageSerializer()  # Nested serializer for the Image model

    class Meta:
        model = CharacterImage
        fields = [
            "id",
            "character",
            "character_full_name",
            "character_race",
            "image",
            "created_at",
            "updated_at",
        ]

    def get_character_full_name(self, obj):
        """
        Returns the full name of the character.
        """
        return f"{obj.character.first_name} {obj.character.last_name}"
