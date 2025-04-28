from rest_framework import serializers
from .models import TableHeader
from npc_system.models import (
    NpcSystem,
)  # Import the NpcSystem class MODELNAME(models.Model):


class TableHeaderSerializer(serializers.ModelSerializer):
    """
    Serializer for the TableHeader model.
    """

    class Meta:
        model = TableHeader
        fields = (
            "id",
            "npc_system",
            "name",
            "description",
            "report_display_heading",
            "display_order",
            "number_of_rolls",
            "roll_die_type",
            "roll_mod",
            "random_gen_inclusision_level",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("created_at", "updated_at", "id")
