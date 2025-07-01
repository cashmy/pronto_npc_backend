from rest_framework import serializers

from .models import Character


class CharacterSerializer(serializers.ModelSerializer):
    """
    Serializer for the Character model.

    This serializer handles the conversion of Character model instances to and from
    JSON format. It includes read-only fields to display names of related objects
    (like NPC system, character group, etc.) instead of just their IDs, enhancing
    the readability of the API output. It also includes write-only fields for
    foreign keys to simplify the creation and update process.

    Attributes:
        id (int): The unique identifier for the character.
        first_name (str): The first name of the character.
        last_name (str): The last name of the character.
        alias (str, optional): An alias or nickname for the character.
        age_category_description (str, optional): A description of the character's age category.
        age (int, optional): The numerical age of the character.
        race (str, optional): The race of the character.
        profession (str, optional): The profession of the character.
        rpg_class (str, optional): The RPG class of the character.
        gender (str, optional): The gender of the character.
        bulk_generated (bool): Flag indicating if the character was bulk-generated.
        reviewed (bool): Flag indicating if the character has been reviewed.
        current_location (str, optional): The current location of the character.
        description (str, optional): A detailed description of the character.
        notes (str, optional): Additional notes about the character.
        npc_system (int): The ID of the associated NPC system (write-only).
        character_sub_group (int): The ID of the associated character sub-group (write-only).
        character_group (int): The ID of the associated character group (write-only).
        archetype (int, optional): The ID of the associated archetype (write-only).
        ai_integration_exists (bool): Flag indicating if AI integration exists.
        owner (int, optional): The ID of the user who owns the character.
        created_at (datetime): The timestamp of creation.
        updated_at (datetime): The timestamp of the last update.
    """

    class Meta:
        """Metadata options for the CharacterSerializer."""

        model = Character
        fields = [
            "id",
            "first_name",
            "last_name",
            "alias",
            "age_category_description",
            "age",
            "race",
            "profession",
            "rpg_class",
            "gender",
            "bulk_generated",
            "reviewed",
            "current_location",
            "description",
            "notes",
            "npc_system",
            "character_sub_group",
            "character_group",
            "archetype",
            "ai_integration_exists",
            "owner",
            "created_at",
            "updated_at",
            # Add read-only fields for display names
            "npc_system_name",
            "npc_system_color",
            "character_group_display_name",
            "character_sub_group_display_name",
            "archetype_name",
        ]
        read_only_fields = [
            "id",
            "npc_system_name",
            "npc_system_color",
            "character_group_display_name",
            "character_sub_group_display_name",
            "archetype_name",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "first_name": {"required": True, "allow_blank": False},
            "last_name": {"required": True, "allow_blank": False},
            "age": {"required": False, "allow_null": True},
            # Make FKs write-only in the API representation if desired
            "npc_system": {"write_only": True},
            "character_group": {"write_only": True},
            "character_sub_group": {"write_only": True},
            # Archetype is already optional due to model's null=True, blank=True
            # but making it write_only improves the read representation
            "archetype": {"required": False, "allow_null": True, "write_only": True},
        }

    # Add fields to display related object names
    npc_system_name = serializers.CharField(
        source="npc_system.npc_system_name", read_only=True
    )
    npc_system_color = serializers.CharField(
        source="npc_system.npc_system_color", read_only=True
    )  # Display the NPC system name instead of the ID

    character_group_display_name = serializers.SerializerMethodField(read_only=True)
    character_sub_group_display_name = serializers.SerializerMethodField(read_only=True)
    archetype_name = serializers.CharField(
        source="archetype.name", read_only=True, allow_null=True
    )

    def get_character_group_display_name(self, obj):
        """
        Get the display name for the character's group.

        Uses the short name if available, otherwise falls back to the full name.

        Args:
            obj (Character): The character instance.

        Returns:
            str or None: The display name of the character group.
        """
        group = obj.character_group
        if group:
            return (
                group.character_group_short_name
                if group.character_group_short_name
                else group.character_group_name
            )
        return None

    def get_character_sub_group_display_name(self, obj):
        """
        Get the display name for the character's sub-group.

        Uses the short name if available, otherwise falls back to the full name.

        Args:
            obj (Character): The character instance.

        Returns:
            str or None: The display name of the character sub-group.
        """
        sub_group = obj.character_sub_group
        if sub_group:
            return (
                sub_group.character_sub_group_short_name
                if sub_group.character_sub_group_short_name
                else sub_group.character_sub_group_name
            )
        return None

    # Add validation if needed, e.g., ensure sub_group belongs to group
    def validate(self, data):
        """
        Validate the relationships between related objects.

        Ensures that the selected sub-group belongs to the selected group, and
        the selected group belongs to the selected NPC system.

        Args:
            data (dict): The data to validate.

        Returns:
            dict: The validated data.
        """
        # Example validation: Ensure the selected sub_group belongs to the selected group
        group = data.get("character_group")
        sub_group = data.get("character_sub_group")

        if group and sub_group and sub_group.character_group != group:
            raise serializers.ValidationError(
                {
                    "character_sub_group": "This sub-group does not belong to the selected character group."
                }
            )

        # Example validation: Ensure the selected group belongs to the selected system
        system = data.get("npc_system")
        if system and group and group.npc_system != system:
            raise serializers.ValidationError(
                {
                    "character_group": "This group does not belong to the selected NPC system."
                }
            )

        # You might add similar validation for archetype if it's tied to a system/group

        return data
