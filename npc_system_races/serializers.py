from rest_framework import serializers
from npc_system_races.models import NpcSystemRace


class NpcSystemRaceSerializer(serializers.ModelSerializer):
    """Serializes NpcSystemRace data for API endpoints.

    This serializer defines the primary data contract for the NpcSystemRace
    model, including read-only fields for related data to provide more
    context in API responses.

    Attributes:
        id (int): The unique primary key for the race instance. Read-only.
        race_id (int): A unique, sequential identifier for the race within
            its parent NpcSystem. Read-only.
        npc_system (int): The primary key of the parent
            :class:`~npc_system.models.NpcSystem`. Write-only.
        npc_system_name (str): The name of the parent NPC system. Read-only.
        race_table_header (str): The race table header from the parent
            NPC system. Read-only.
        value (str): The name of the race (e.g., "Human", "Elf").
    """

    npc_system_name = serializers.CharField(
        source="npc_system.npc_system_name", read_only=True
    )
    race_table_header = serializers.CharField(
        source="npc_system.race_table_header", read_only=True
    )

    class Meta:
        model = NpcSystemRace
        fields = [
            "id",
            "race_id",
            "npc_system",
            "npc_system_name",
            "race_table_header",
            "value",
        ]


class NpcSystemRaceOptionSerializer(serializers.ModelSerializer):
    """Provides a simplified representation of races for dropdowns.

    This serializer exposes only the fields necessary for populating a
    select/option list in a frontend application, making it lightweight.

    Attributes:
        race_id (int): The unique, sequential identifier for the race within
            its parent NpcSystem.
        value (str): The name of the race (e.g., "Human", "Elf").
    """
    class Meta:
        model = NpcSystemRace
        fields = ["race_id", "value"]
