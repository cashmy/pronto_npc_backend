# d:\Python-Django\pronto_npc_backend\character_group\serializers.py
from rest_framework import serializers
from .models import CharacterGroup

# Optional: Import NpcSystem if needed for deeper validation or representation,
# but ModelSerializer handles the ForeignKey relationship by default.
# from npc_system.models import NpcSystem


class CharacterGroupSerializer(serializers.ModelSerializer):
    """
    Serializer for the CharacterGroup model.
    """

    # Optional: Display the related system's name for better readability in GET requests
    npc_system_name = serializers.CharField(
        source="npc_system.npc_system_name", read_only=True
    )

    class Meta:
        model = CharacterGroup
        fields = [
            "id",
            "npc_system",  # Foreign key ID (writable)
            "npc_system_name",  # Related system name (read-only)
            "character_group_name",
            "character_group_short_name",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "npc_system_name",  # Read-only as it's derived
            "created_at",
            "updated_at",
            # 'character_group_short_name', # Keep writable if users can override,
            # or make read-only if it's always auto-generated
        ]
        extra_kwargs = {
            # Make the 'npc_system' ID field write-only in the API representation,
            # as we display 'npc_system_name' for reading.
            "npc_system": {"write_only": True}
        }

    # No custom 'create' or 'validate' methods are needed here based on the
    # NpcSystemSerializer example, unless you have specific logic for CharacterGroup
    # (e.g., validation based on the related NpcSystem or user permissions).
    # The default short_name logic, if implemented in the model's save() method,
    # will be handled automatically.
