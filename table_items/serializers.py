from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from table_items.models import TableItem
from npc_system.models import NpcSystem


class TableItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the TableItems model.
    """

    npc_system = serializers.PrimaryKeyRelatedField(
        queryset=NpcSystem.objects.all(),
        required=False,  # Will be derived from table_header if not provided
        allow_null=False,  # Model field is not nullable
    )

    npc_system_name = serializers.CharField(
        source="npc_system.npc_system_name", read_only=True
    )  # Display the NPC system name instead of the ID

    table_header_name = serializers.CharField(
        source="table_header.name", read_only=True
    )  # Display the table header name instead of the ID

    subsequent_table_name = serializers.CharField(
        source="subsequent_table.name", read_only=True, allow_null=True
    )

    class Meta:
        model = TableItem
        fields = (
            "id",
            "npc_system",
            "npc_system_name",
            "table_header",
            "table_header_name",
            "item_id",  # Read-only, auto-generated
            "value",
            "reroll_this_item",
            "description",
            "notes",
            "subsequent_table_roll",
            "subsequent_table",
            "subsequent_table_name",  # Display only
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "item_id",
            "created_at",
            "updated_at",
            "npc_system_name",
            "table_header_name",
            "subsequent_table_name",
        )

    def validate(self, attrs):
        # Determine effective value for subsequent_table_roll
        subsequent_table_roll = attrs.get("subsequent_table_roll", None)
        if subsequent_table_roll is None:
            if self.instance:
                subsequent_table_roll = self.instance.subsequent_table_roll
            else:
                subsequent_table_roll = self.Meta.model._meta.get_field(
                    "subsequent_table_roll"
                ).get_default()

        # Determine effective table_header (must be present for validation logic)
        # table_header is required on POST by default PrimaryKeyRelatedField behavior.
        # On PATCH/PUT, if not in attrs, use instance's.
        final_table_header = attrs.get(
            "table_header", getattr(self.instance, "table_header", None)
        )

        if not final_table_header:
            # This should ideally be caught by DRF's field validation for table_header being required on create.
            # If table_header is None here, subsequent validations might fail or be incomplete.
            # For safety, if creating and table_header is missing:
            if self.instance is None:
                raise serializers.ValidationError(
                    {"table_header": _("This field is required.")}
                )

        # --- subsequent_table validation ---
        # Get the subsequent_table from attrs if present, otherwise from instance (if not changing)
        effective_subsequent_table = (
            attrs.get("subsequent_table")
            if "subsequent_table" in attrs
            else (
                getattr(self.instance, "subsequent_table", None)
                if self.instance
                else None
            )
        )

        if subsequent_table_roll:
            if effective_subsequent_table is None:
                raise serializers.ValidationError(
                    {
                        "subsequent_table": _(
                            "This field is required and cannot be null when 'subsequent_table_roll' is true."
                        )
                    }
                )
            if (
                final_table_header
                and effective_subsequent_table.id == final_table_header.id
            ):
                raise serializers.ValidationError(
                    {
                        "subsequent_table": _(
                            "The subsequent table cannot be the same as the item's parent table header."
                        )
                    }
                )
        else:  # subsequent_table_roll is False
            # If flag is false, subsequent_table should be None.
            # Case 1: User explicitly provides a non-null subsequent_table in the payload.
            if "subsequent_table" in attrs and attrs["subsequent_table"] is not None:
                raise serializers.ValidationError(
                    {
                        "subsequent_table": _(
                            "A subsequent table cannot be specified when 'subsequent_table_roll' is false. Set this to null or omit."
                        )
                    }
                )
            # Case 2: Flag is false, subsequent_table NOT in payload, but instance has one. Auto-clear.
            elif (
                "subsequent_table" not in attrs
                and self.instance
                and self.instance.subsequent_table is not None
            ):
                attrs["subsequent_table"] = None  # Ensure it's cleared on save.

        # --- NpcSystem Consistency & Derivation ---
        if final_table_header:  # Should always be true if table_header is required
            if "npc_system" in attrs:
                # User provided an npc_system. Validate it.
                provided_npc_system = attrs["npc_system"]
                if (
                    provided_npc_system is None
                ):  # Should be caught by allow_null=False on serializer field
                    raise serializers.ValidationError(
                        {"npc_system": _("NpcSystem cannot be null.")}
                    )
                if final_table_header.npc_system_id != provided_npc_system.id:
                    raise serializers.ValidationError(
                        {
                            "npc_system": _(
                                f"The provided NpcSystem ('{provided_npc_system.npc_system_name}') "
                                f"does not match the NpcSystem of the selected TableHeader ('{final_table_header.npc_system.npc_system_name}')."
                            )
                        }
                    )
            else:
                # npc_system not provided in payload. Derive it from final_table_header.
                # This handles create (self.instance is None) and update (if npc_system field is omitted in PATCH).
                attrs["npc_system"] = final_table_header.npc_system
        elif self.instance is None:  # Creating and final_table_header is somehow None
            # This indicates table_header was not provided or invalid on create, which DRF should have caught.
            raise serializers.ValidationError(
                {
                    "npc_system": _(
                        "Cannot determine NpcSystem as TableHeader is missing or invalid."
                    )
                }
            )

        return attrs
