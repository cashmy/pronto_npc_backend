from rest_framework import serializers
from table_items.models import TableItem


class TableItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the TableItems model.
    """

    npc_system_name = serializers.CharField(
        source="npc_system.npc_system_name", read_only=True
    )  # Display the NPC system name instead of the ID

    table_header_name = serializers.CharField(
        source="table_header.name", read_only=True
    )  # Display the table header name instead of the ID

    subsequent_table = serializers.CharField(source="table_header.name", read_only=True)

    class Meta:
        model = TableItem
        fields = (
            "id",
            "table_header",
            "value",
            "reroll_this_item",
            "description",
            "notes",
            "subsequent_table_roll",
            "subsequent_table",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("created_at", "updated_at", "id")
