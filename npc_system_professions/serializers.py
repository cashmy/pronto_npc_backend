from rest_framework import serializers
from npc_system_professions.models import NpcSystemProfession


class NpcSystemProfessionSerializer(serializers.ModelSerializer):
    """Serializes NpcSystemProfession data for API endpoints.

    This serializer defines the primary data contract for the NpcSystemProfession
    model, including read-only fields for related data to provide more
    context in API responses.

    Attributes:
        id (int): The unique primary key for the profession instance. Read-only.
        profession_id (int): A unique, sequential identifier for the profession
            within its parent NpcSystem. Read-only.
        npc_system (int): The primary key of the parent
            :class:`~npc_system.models.NpcSystem`. Write-only.
        npc_system_name (str): The name of the parent NPC system. Read-only.
        profession_table_header (str): The profession table header from the
            parent NPC system. Read-only.
        value (str): The name of the profession (e.g., "Blacksmith", "Hunter").
    """

    npc_system_name = serializers.CharField(
        source="npc_system.npc_system_name", read_only=True
    )
    profession_table_header = serializers.CharField(
        source="npc_system.profession_table_header", read_only=True
    )

    class Meta:
        model = NpcSystemProfession
        fields = [
            "id",
            "profession_id",
            "npc_system",
            "npc_system_name",
            "profession_table_header",
            "value",
        ]


# Serializer for the dropdown options in the frontend
class NpcSystemProfessionOptionSerializer(serializers.ModelSerializer):
    """Provides a simplified representation of professions for dropdowns.

    This serializer exposes only the fields necessary for populating a
    select/option list in a frontend application, making it lightweight.

    Attributes:
        profession_id (int): The unique, sequential identifier for the profession
            within its parent NpcSystem.
        value (str): The name of the profession (e.g., "Blacksmith", "Hunter").
    """

    class Meta:
        model = NpcSystemProfession
        fields = ["profession_id", "value"]
