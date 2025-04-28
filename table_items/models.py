from django.db import models, transaction
from django.db.models import Max, F  # Import F for potential use later if needed
from npc_system.models import NpcSystem
from table_header.models import TableHeader
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


# Create your models here.
class TableItem(models.Model):
    """
    Represents an item in a table (TableHeader).
    item_id is intended to be unique and sequential within its parent table_header.
    """

    npc_system = models.ForeignKey(
        NpcSystem,
        on_delete=models.CASCADE,
        related_name="table_items",
        help_text=_("The NPC system this table item belongs to."),
    )
    table_header = models.ForeignKey(
        TableHeader,
        on_delete=models.CASCADE,  # If the parent TableHeader is deleted, delete its items
        related_name="table_items",
        help_text=_("The parent table header this item belongs to."),
    )
    # This ID should be unique *within* the table_header
    item_id = models.PositiveIntegerField(
        editable=False,  # Usually not directly edited once set
        db_index=True,  # Index for lookups and uniqueness constraint
        help_text=_(
            "Auto-incrementing ID within the context of the parent table header."
        ),
        # null=True/blank=True technically not needed if save always sets it,
        # but safer to allow temporary null state before first save.
        # The unique_together constraint prevents permanent nulls if needed.
        # Let's keep them for flexibility during object creation in memory.
        null=True,
        blank=True,
    )
    value = models.TextField(
        blank=False,
        null=False,
        help_text=_("The result text or value for this item."),
    )
    reroll_this_item = models.BooleanField(
        default=False,
        help_text=_(
            "Indicates if rolling this specific item should trigger an immediate re-roll on the *same* table."
        ),
    )
    description = models.TextField(
        blank=True,
        help_text=_("Optional description providing more context for the item value."),
    )
    notes = models.TextField(
        blank=True,
        help_text=_("Internal notes about this item, not usually shown to the user."),
    )

    subsequent_table_roll = models.BooleanField(
        default=False,
        help_text=_(
            "Indicates if rolling this item should trigger a roll on the linked subsequent table."
        ),
    )
    subsequent_table = models.ForeignKey(
        TableHeader,
        on_delete=models.SET_NULL,  # If the linked table is deleted, just remove the link
        related_name="source_items_for_subsequent_roll",  # Clearer reverse name
        null=True,
        blank=True,
        help_text=_(
            "Optional: The next table header to roll on if 'subsequent_table_roll' is True."
        ),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        help_text=_("Timestamp when this item was created."),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        help_text=_("Timestamp when this item was last updated."),
    )

    def save(self, *args, **kwargs):
        """
        Override save to ensure item_id is unique and sequential within the table_header.
        Uses a transaction and select_for_update to prevent race conditions.
        """
        # Ensure item_id is set only on the first save (i.e., when pk is None)
        # and only if table_header is actually set.
        if self.pk is None and self.table_header_id is not None:
            try:
                # Use a transaction to ensure atomicity
                with transaction.atomic():
                    # Lock rows for the specific table_header to prevent race conditions
                    # This requires database support (e.g., PostgreSQL, MySQL with InnoDB)
                    existing_items = TableItem.objects.select_for_update().filter(
                        table_header=self.table_header
                    )
                    # Calculate the next item_id
                    max_id_result = existing_items.aggregate(Max("item_id"))
                    max_id = max_id_result.get("item_id__max") or 0
                    self.item_id = max_id + 1
                    # Proceed with the actual save within the transaction
                    super().save(*args, **kwargs)
            except Exception as e:
                # Handle potential exceptions during the transaction
                # You might want specific error handling or logging here
                raise ValidationError(
                    f"Failed to assign sequential item_id: {e}"
                ) from e
        else:
            # If it's an update (self.pk is not None) or table_header isn't set,
            # just perform a regular save.
            # We don't recalculate item_id on updates.
            super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the TableItem instance.
        """
        npc_system_name = (
            self.npc_system.npc_system_name if self.npc_system else "Orphaned System"
        )
        table_header_name = (
            self.table_header.name if self.table_header else "Orphaned Table"
        )
        value_display = (
            (self.value[:47] + "...") if len(self.value) > 50 else self.value
        )
        # Include item_id in the string representation for clarity
        item_id_display = f" (Item {self.item_id})" if self.item_id is not None else ""
        return f"{npc_system_name} - {table_header_name} {item_id_display} - {value_display}"

    class Meta:
        verbose_name = _("Table Item")
        verbose_name_plural = _("Table Items")
        # Order primarily by the parent table, then by the intended display order,
        # using item_id as a fallback tie-breaker if display_order is the same.
        ordering = ["npc_system", "table_header_id", "item_id"]
        # Enforce uniqueness for the combination of table_header and item_id
        unique_together = ("table_header", "item_id")
        # Note: The unique_together constraint implicitly creates a database index.
