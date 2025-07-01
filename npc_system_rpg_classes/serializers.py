from rest_framework import serializers
from .models import NpcSystemRpgClass
 
 
class NpcSystemRpgClassSerializer(serializers.ModelSerializer):
    """Serializes NpcSystemRpgClass data for API endpoints.
 
    This serializer defines the primary data contract for the NpcSystemRpgClass
    model, including read-only fields for related data to provide more
    context in API responses.
 
    Attributes:
        id (int): The unique primary key for the RPG class instance. Read-only.
        rpg_class_id (int): A unique, sequential identifier for the RPG class
            within its parent NpcSystem. Read-only.
        npc_system (int): The primary key of the parent
            :class:`~npc_system.models.NpcSystem`. Write-only.
        npc_system_name (str): The name of the parent NPC system. Read-only.
        rpg_class_table_header (str): The RPG class table header from the parent
            NPC system. Read-only.
        value (str): The name of the RPG class (e.g., "Fighter", "Mage").
    """
 
    npc_system_name = serializers.CharField(
        source="npc_system.npc_system_name", read_only=True
    )
    rpg_class_table_header = serializers.CharField(
        source="npc_system.rpg_class_table_header", read_only=True
    )
 
    class Meta:
        model = NpcSystemRpgClass
        fields = [
            "id",
            "rpg_class_id",
            "npc_system",
            "npc_system_name",
            "rpg_class_table_header",
            "value",
        ]
 
 
# Serializer for the dropdown options in the frontend
class NpcSystemRpgClassOptionSerializer(serializers.ModelSerializer):
    """Provides a simplified representation of RPG classes for dropdowns.
 
    This serializer exposes only the fields necessary for populating a
    select/option list in a frontend application, making it lightweight.
 
    Attributes:
        rpg_class_id (int): The unique, sequential identifier for the RPG class
            within its parent NpcSystem.
        value (str): The name of the RPG class (e.g., "Fighter", "Mage").
    """
 
    class Meta:
        model = NpcSystemRpgClass
        fields = ["rpg_class_id", "value"]
