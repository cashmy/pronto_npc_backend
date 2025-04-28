from rest_framework import serializers
from table_group.models import TableGroup


class TableGroupSerializer(serializers.ModelSerializer):

    npc_system_name = serializers.CharField(
        source="npc_system.npc_system_name", read_only=True
    )  # Display the NPC system name instead of the ID

    class Meta:
        model = TableGroup
        fields = (
            "id",
            "npc_system",
            "name",
            "description",
            "report_display_heading",
            "display_order",
            "number_of_rolls",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("created_at", "updated_at", "id")

    def create(self, validated_data):
        return TableGroup.objects.create(**validated_data)
