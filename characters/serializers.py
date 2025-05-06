from rest_framework import serializers
from .models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = [
            "id",
            "first_name",
            "last_name",
            "alias",
            "age_category_description",
            "age",
            "race",
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
            "created_at",
            "updated_at",
            # Add read-only fields for display names
            "npc_system_name",
            "character_group_display_name",
            "character_sub_group_display_name",
            "archetype_name",
        ]
        read_only_fields = [
            "id",
            "npc_system_name",
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
    character_group_display_name = serializers.SerializerMethodField(read_only=True)
    character_sub_group_display_name = serializers.SerializerMethodField(read_only=True)
    archetype_name = serializers.CharField(
        source="archetype.name", read_only=True, allow_null=True
    )

    def get_character_group_display_name(self, obj):
        group = obj.character_group
        if group:
            return (
                group.character_group_short_name
                if group.character_group_short_name
                else group.character_group_name
            )
        return None

    def get_character_sub_group_display_name(self, obj):
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
