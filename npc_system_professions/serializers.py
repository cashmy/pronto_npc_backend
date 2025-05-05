from rest_framework import serializers
from npc_system_professions.models import NpcSystemProfession


class NpcSystemProfessionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profession model.
    Includes the NPC system name for better readability.
    """

    npc_system_name = serializers.CharField(
        source="npc_system.npc_system_name", read_only=True
    )  # Display the NPC system name instead of the ID
    profession_table_header = serializers.CharField(
        source="npc_system.profession_table_header", read_only=True
    )

    class Meta:
        model = NpcSystemProfession
        fields = [
            "id",  # Auto-incrementing ID within the NPC system
            "profession_id",  # Unique ID within the NPC system - sequential
            "npc_system",  # FK to the NPC system
            "npc_system_name",  # Readable name of the NPC system
            "profession_table_header",  # Header for the profession table
            "value",  # The profession name
        ]
        read_only_fields = ["id"]  # ID is auto-generated


# Serializer for the dropdown options in the frontend
class NpcSystemProfessionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NpcSystemProfession
        fields = ["profession_id", "value"]
