from rest_framework import serializers
from npc_system_races.models import NpcSystemRace


class NpcSystemRaceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Race model.
    Includes the NPC system name for better readability.
    """

    npc_system_name = serializers.CharField(
        source="npc_system.npc_system_name", read_only=True
    )  # Display the NPC system name instead of the ID
    race_table_header = serializers.CharField(
        source="npc_system.race_table_header", read_only=True
    )

    class Meta:
        model = NpcSystemRace
        fields = [
            "id",  # Auto-incrementing ID within the NPC system
            "race_id",  # Unique ID within the NPC system - sequential
            "npc_system",  # FK to the NPC system
            "npc_system_name",  # Readable name of the NPC system
            "race_table_header",  # Header for the race table
            "value",  # The race name
        ]
        read_only_fields = ["id"]  # ID is auto-generated


# Serializer for the dropdown options in the frontend
class NpcSystemRaceOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NpcSystemRace
        fields = ["race_id", "value"]
