from rest_framework import serializers
from .models import TableHeader
from npc_system.models import NpcSystem
from table_group.models import TableGroup


class TableHeaderSerializer(serializers.ModelSerializer):
    """
    Serializer for the TableHeader model.
    """

    # --- Input Fields (for POST/PUT) ---
    # These are write_only; their values are processed in validate()
    # to populate the actual 'npc_system' and 'table_group' model fields.
    npc_system_id = serializers.PrimaryKeyRelatedField(
        queryset=NpcSystem.objects.all(),
        required=False,
        write_only=True,
        allow_null=True,
        help_text="Provide EITHER NpcSystem ID.",
    )
    npc_system_name = serializers.SlugRelatedField(
        queryset=NpcSystem.objects.all(),
        slug_field="npc_system_name",
        required=False,
        write_only=True,
        allow_null=True,
        help_text="OR NpcSystem Name.",
    )
    table_group_id = serializers.PrimaryKeyRelatedField(
        queryset=TableGroup.objects.all(),
        required=False,
        write_only=True,
        allow_null=True,
        help_text="Provide EITHER TableGroup ID.",
    )
    table_group_name = (
        serializers.SlugRelatedField(  # Renamed from table_group_display_name
            queryset=TableGroup.objects.all(),
            slug_field="name",
            required=False,
            write_only=True,
            allow_null=True,
            help_text="OR TableGroup Name.",
        )
    )

    # --- Output Fields (for GET) ---
    # 'npc_system' and 'table_group' from Meta.fields will output IDs.
    # These provide the names for GET requests.
    display_npc_system_name = serializers.CharField(
        source="npc_system.npc_system_name", read_only=True
    )
    display_table_group_name = serializers.CharField(
        source="table_group.name", read_only=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = TableHeader
        fields = (
            "id",
            "npc_system",
            "npc_system_id",  # Add write_only input field
            "npc_system_name",  # Add write_only input field
            "display_npc_system_name",
            "table_group",
            "table_group_id",  # Add write_only input field
            "table_group_name",  # Add write_only input field
            "display_table_group_name",
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
        read_only_fields = (
            "id",
            "npc_system",  # Mark as read-only for input purposes
            "table_group",  # Mark as read-only for input purposes
            "created_at",
            "updated_at",
            "display_npc_system_name",
            "display_table_group_name",
        )
        extra_kwargs = {
            # These are the actual model FK fields.
            # Make them not required at serializer level so validate() can populate them.
            "npc_system": {"required": False, "allow_null": True},
            "table_group": {"required": False, "allow_null": True},
        }

    def validate(self, attrs):
        # attrs contains data from all fields, including write_only ones.
        # It also includes 'npc_system' and 'table_group' as None due to extra_kwargs.

        # Pop input values (these are already resolved to model instances or None by DRF fields)
        npc_system_via_id = attrs.pop("npc_system_id", None)
        npc_system_via_name = attrs.pop("npc_system_name", None)
        table_group_via_id = attrs.pop("table_group_id", None)
        table_group_via_name = attrs.pop("table_group_name", None)

        resolved_table_group = None
        resolved_npc_system = None

        # 1. Resolve TableGroup
        if table_group_via_id and table_group_via_name:
            if table_group_via_id != table_group_via_name:
                raise serializers.ValidationError(
                    {
                        "table_group_id": "ID and Name for TableGroup do not match.",
                        "table_group_name": "ID and Name for TableGroup do not match.",
                    }
                )
            resolved_table_group = table_group_via_id
        elif table_group_via_id:
            resolved_table_group = table_group_via_id
        elif table_group_via_name:
            resolved_table_group = table_group_via_name
        else:
            # Assign error to a specific field for better client feedback
            raise serializers.ValidationError(
                {
                    "table_group_name": "Either 'table_group_id' or 'table_group_name' is required.",
                    "table_group_id": "Either 'table_group_id' or 'table_group_name' is required.",
                }
            )

        if not resolved_table_group:  # Should be caught by above, but as a safeguard
            raise serializers.ValidationError(
                {"table_group_name": "TableGroup could not be resolved or is missing."}
            )

        # 2. Resolve NpcSystem
        if npc_system_via_id and npc_system_via_name:
            if npc_system_via_id != npc_system_via_name:
                raise serializers.ValidationError(
                    {
                        "npc_system_id": "ID and Name for NpcSystem do not match.",
                        "npc_system_name": "ID and Name for NpcSystem do not match.",
                    }
                )
            resolved_npc_system = npc_system_via_id
        elif npc_system_via_id:
            resolved_npc_system = npc_system_via_id
        elif npc_system_via_name:
            resolved_npc_system = npc_system_via_name
        else:
            # Try to derive from resolved_table_group
            if (
                resolved_table_group
                and hasattr(resolved_table_group, "npc_system")
                and resolved_table_group.npc_system
            ):
                resolved_npc_system = resolved_table_group.npc_system
            else:
                # This error occurs if NpcSystem cannot be determined at all.
                raise serializers.ValidationError(
                    {
                        "npc_system_name": (  # Or npc_system_id, pointing to user input options
                            "NpcSystem is required. Provide 'npc_system_id' or 'npc_system_name', "
                            "or ensure the selected TableGroup has an associated NpcSystem (and it's not None)."
                        )
                    }
                )

        if not resolved_npc_system:  # Safeguard
            raise serializers.ValidationError(
                {"npc_system_name": "NpcSystem could not be resolved or is missing."}
            )

        # 3. Consistency Check: Ensure the derived/provided NpcSystem matches the TableGroup's NpcSystem
        if resolved_table_group.npc_system != resolved_npc_system:
            raise serializers.ValidationError(
                f"The provided or derived NpcSystem ('{resolved_npc_system.npc_system_name}') does not match "
                f"the NpcSystem ('{resolved_table_group.npc_system.npc_system_name}') of the selected TableGroup ('{resolved_table_group.name}')."
            )

        # Populate the actual model fields in attrs for ModelSerializer to use
        attrs["table_group"] = resolved_table_group
        attrs["npc_system"] = resolved_npc_system
        return attrs
