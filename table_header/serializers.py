from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .models import TableHeader
from npc_system.models import NpcSystem
from table_group.models import TableGroup


class TableHeaderSerializer(serializers.ModelSerializer):
    """
    Serializer for the TableHeader model.
    Handles creation and updates, allowing NpcSystem and TableGroup
    to be specified by ID or by name, and deriving NpcSystem from
    TableGroup if not explicitly provided on creation.
    """

    # Explicitly define model FK fields for more control over input behavior
    # These allow direct ID input and are made not strictly required in the payload
    # because their values can be derived or come from name-based fields.
    npc_system = serializers.PrimaryKeyRelatedField(
        queryset=NpcSystem.objects.all(),
        required=False,
        allow_null=True,  # Allows payload to explicitly set to null
        help_text="Direct ID of the NpcSystem. Alternatively, use 'npc_system_name'.",
    )
    table_group = serializers.PrimaryKeyRelatedField(
        queryset=TableGroup.objects.all(),
        required=False,
        allow_null=True,  # Allows payload to explicitly set to null
        help_text="Direct ID of the TableGroup. Alternatively, use 'table_group_name'.",
    )

    # --- Input Helper Fields (for POST/PUT/PATCH by name) ---
    # These are write_only; their values are processed in validate()
    npc_system_name = serializers.SlugRelatedField(
        queryset=NpcSystem.objects.all(),
        slug_field="npc_system_name",
        required=False,
        write_only=True,
        allow_null=True,  # Allows payload to explicitly set to null
        help_text="To specify NpcSystem by name (alternative to providing 'npc_system' ID directly).",
    )
    table_group_name = serializers.SlugRelatedField(
        queryset=TableGroup.objects.all(),
        slug_field="name",
        required=False,
        write_only=True,
        allow_null=True,  # Allows payload to explicitly set to null
        help_text="To specify TableGroup by name (alternative to providing 'table_group' ID directly).",
    )

    # --- Output Display Fields (for GET) ---
    # These provide the names for GET requests.
    display_npc_system_name = serializers.CharField(
        source="npc_system.npc_system_name", read_only=True
    )
    display_table_group_name = serializers.CharField(
        source="table_group.name", read_only=True
    )

    class Meta:
        model = TableHeader
        fields = (
            "id",
            "npc_system",  # For ID input/output
            "npc_system_name",  # For name input (write_only)
            "display_npc_system_name",  # For name output (read_only)
            "table_group",  # For ID input/output
            "table_group_name",  # For name input (write_only)
            "display_table_group_name",  # For name output (read_only)
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
            "created_at",
            "updated_at",
            "display_npc_system_name",
            "display_table_group_name",
        )
        # Note: `npc_system_name` and `table_group_name` are write_only as defined above,
        # so they don't need to be in read_only_fields.

    def validate(self, attrs):
        print(f"DEBUG: validate() called with attrs: {attrs}")
        is_update = self.instance is not None

        # Get values from direct ID input fields (already resolved to objects by DRF if IDs were valid)
        npc_system_from_direct_id = attrs.get("npc_system")
        table_group_from_direct_id = attrs.get("table_group")

        # Get values from helper name input fields (already resolved to objects by DRF if names were valid)
        npc_system_from_name_field_obj = attrs.get("npc_system_name")
        table_group_from_name_field_obj = attrs.get("table_group_name")

        resolved_table_group = None
        resolved_npc_system = None

        # --- 1. Resolve TableGroup ---
        if (
            table_group_from_direct_id is not None
            and table_group_from_name_field_obj is not None
        ):
            if table_group_from_direct_id != table_group_from_name_field_obj:
                raise serializers.ValidationError(
                    {
                        "table_group": _(
                            "ID provided for 'table_group' and name for 'table_group_name' refer to different objects."
                        ),
                        "table_group_name": _(
                            "Name provided for 'table_group_name' and ID for 'table_group' refer to different objects."
                        ),
                    }
                )
            resolved_table_group = table_group_from_direct_id
        elif table_group_from_direct_id is not None:
            resolved_table_group = table_group_from_direct_id
        elif table_group_from_name_field_obj is not None:
            resolved_table_group = table_group_from_name_field_obj
        elif (
            is_update and "table_group" not in attrs and "table_group_name" not in attrs
        ):
            # For PATCH/PUT, if not provided in payload, use existing instance value
            resolved_table_group = self.instance.table_group
        elif not is_update:  # Create operation
            raise serializers.ValidationError(
                {
                    "table_group": _(
                        "Either 'table_group' (by ID) or 'table_group_name' (by name) is required for creation."
                    ),
                    "table_group_name": _(
                        "Either 'table_group_name' (by name) or 'table_group' (by ID) is required for creation."
                    ),
                }
            )
        # If 'table_group' or 'table_group_name' was explicitly provided as null in payload for an update
        elif is_update and (
            attrs.get("table_group") is None or attrs.get("table_group_name") is None
        ):
            # This path is taken if null was explicitly sent.
            # Model's table_group is non-nullable, so this is an error.
            pass  # Let the null check below handle it.

        # Check if resolved_table_group is None (e.g., explicit null in payload)
        # TableHeader.table_group is a non-nullable ForeignKey
        if resolved_table_group is None:
            raise serializers.ValidationError(
                {"table_group": _("TableGroup is required and cannot be null.")}
            )

        attrs["table_group"] = resolved_table_group
        attrs.pop("table_group_name", None)  # Clean up helper field

        print(f"DEBUG: resolved_table_group: {resolved_table_group}")

        # --- 2. Resolve NpcSystem ---
        if (
            npc_system_from_direct_id is not None
            and npc_system_from_name_field_obj is not None
        ):
            if npc_system_from_direct_id != npc_system_from_name_field_obj:
                raise serializers.ValidationError(
                    {
                        "npc_system": _(
                            "ID provided for 'npc_system' and name for 'npc_system_name' refer to different objects."
                        ),
                        "npc_system_name": _(
                            "Name provided for 'npc_system_name' and ID for 'npc_system' refer to different objects."
                        ),
                    }
                )
            resolved_npc_system = npc_system_from_direct_id
        elif npc_system_from_direct_id is not None:
            resolved_npc_system = npc_system_from_direct_id
        elif npc_system_from_name_field_obj is not None:
            resolved_npc_system = npc_system_from_name_field_obj
        elif is_update and "npc_system" not in attrs and "npc_system_name" not in attrs:
            # For PATCH/PUT, if not provided in payload, use existing instance value
            resolved_npc_system = self.instance.npc_system
        elif not is_update:  # Create operation - try to derive
            if (
                resolved_table_group
                and hasattr(resolved_table_group, "npc_system")
                and resolved_table_group.npc_system
            ):
                resolved_npc_system = resolved_table_group.npc_system
            else:
                raise serializers.ValidationError(
                    {
                        "npc_system": _(
                            "NpcSystem is required for creation. Provide 'npc_system' (by ID), 'npc_system_name' (by name), or ensure the selected TableGroup has an associated NpcSystem."
                        ),
                        "npc_system_name": _(
                            "NpcSystem is required for creation. Provide 'npc_system_name' (by name), 'npc_system' (by ID), or ensure the selected TableGroup has an associated NpcSystem."
                        ),
                    }
                )
        # If 'npc_system' or 'npc_system_name' was explicitly provided as null in payload for an update
        elif is_update and (
            attrs.get("npc_system") is None or attrs.get("npc_system_name") is None
        ):
            # This path is taken if null was explicitly sent.
            # Model's npc_system is non-nullable, so this is an error.
            pass  # Let the null check below handle it.

        # Check if resolved_npc_system is None (e.g., explicit null in payload or failed derivation)
        # TableHeader.npc_system is a non-nullable ForeignKey
        if resolved_npc_system is None:
            raise serializers.ValidationError(
                {"npc_system": _("NpcSystem is required and cannot be null.")}
            )

        attrs["npc_system"] = resolved_npc_system
        attrs.pop("npc_system_name", None)  # Clean up helper field

        print(f"DEBUG: resolved_npc_system: {resolved_npc_system}")

        # --- 3. Consistency Check ---
        # Ensure the derived/provided NpcSystem matches the TableGroup's NpcSystem
        if resolved_table_group.npc_system != resolved_npc_system:
            raise serializers.ValidationError(
                _(
                    "The NpcSystem ('%(resolved_npc_system_name)s') of the TableHeader does not match "
                    "the NpcSystem ('%(table_group_npc_system_name)s') of the selected TableGroup ('%(table_group_name)s')."
                )
                % {
                    "resolved_npc_system_name": resolved_npc_system.npc_system_name,
                    "table_group_npc_system_name": resolved_table_group.npc_system.npc_system_name,
                    "table_group_name": resolved_table_group.name,
                }
            )

        # Remove original direct ID fields if they were None and we resolved through name,
        # to prevent them from being passed as None to the model if they were not in the payload initially.
        # This is more of a cleanup for `attrs` before it's returned.
        if (
            "npc_system" in attrs
            and attrs["npc_system"] is None
            and npc_system_from_direct_id is None
        ):
            # This case should ideally be caught by the "cannot be null" check above if resolved_npc_system ended up None.
            # If resolved_npc_system is not None, then attrs['npc_system'] is already correctly set.
            pass
        if (
            "table_group" in attrs
            and attrs["table_group"] is None
            and table_group_from_direct_id is None
        ):
            # Similar to npc_system, should be caught by the "cannot be null" check.
            pass

        return attrs
