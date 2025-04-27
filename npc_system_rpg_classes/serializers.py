from rest_framework import serializers
from .models import NpcSystemRpgClass


class NpcSystemRpgClassSerializer(serializers.ModelSerializer):
    """
    Serializer for the Rpg Class model.
    Includes the NPC system name for better readability.
    """

    npc_system_name = serializers.CharField(
        source="npc_system.npc_system_name", read_only=True
    )  # Display the NPC system name instead of the ID
    rpg_class_table_header = serializers.CharField(
        source="npc_system.rpg_class_table_header", read_only=True
    )

    class Meta:
        model = NpcSystemRpgClass
        fields = [
            "npc_system",  # FK to the NPC system
            "npc_system_name",  # Readable name of the NPC system
            "rpg_class_table_header",  # Header for the race table
            "id",  # Auto-incrementing ID within the NPC system
            "value",  # The race name
        ]
        read_only_fields = ["id"]  # ID is auto-generated
