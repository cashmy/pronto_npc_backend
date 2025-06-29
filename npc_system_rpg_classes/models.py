"""
Defines the data model for RPG classes within the NPC system.

This module contains the `NpcSystemRpgClass` model, which represents a specific
RPG class (e.g., Warrior, Mage) that can be assigned to an NPC within a
particular game system.
"""

from django.db import models, transaction

from npc_system.models import NpcSystem


class NpcSystemRpgClass(models.Model):
    """
    Represents an RPG Class within a specific NPC system.

    An RPG Class is a role that an NPC can have, such as "Warrior", "Mage", or
    "Thief". Each class is tied to a specific :class:`~npc_system.models.NpcSystem`,
    ensuring that classes are unique and managed within the context of their
    game system.
    """

    npc_system = models.ForeignKey(
        NpcSystem,
        on_delete=models.CASCADE,
        related_name="rpg_classes",
        help_text="The NPC system this RPG Class belongs to.",
    )
    """A reference to the :class:`~npc_system.models.NpcSystem` this class belongs to."""

    rpg_class_id = models.PositiveIntegerField(
        editable=False,  # Usually not directly edited once set
        db_index=True,  # Index for lookups and uniqueness constraint
        help_text="Auto-incrementing ID within the context of the NPC system.",
        # null=True/blank=True technically not needed if save always sets it,
        # but safer to allow temporary null state before first save.
        # The unique_together constraint prevents permanent nulls if needed.
        # Let's keep them for flexibility during object creation in memory.
        blank=True,
        null=True,
    )
    """A sequential, system-specific ID that is automatically assigned upon creation."""

    value = models.CharField(
        max_length=25,
        help_text="The name of the class (e.g., Warrior, Thief, Mage).",
    )
    """The name of the RPG class (e.g., "Warrior")."""

    class Meta:
        """Meta options for the NpcSystemRpgClass model."""

        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ["npc_system", "id"]
        # Ensures rpg_class_id is unique within the scope of an npc_system.
        unique_together = ("npc_system", "rpg_class_id")

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to manage `rpg_class_id`.

        If `rpg_class_id` is not already set, this method assigns a new,
        sequential ID within the context of the parent `npc_system`. It uses a
        database transaction with `select_for_update` to lock the relevant
        rows, preventing race conditions when multiple classes are created
        concurrently for the same system.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if not self.rpg_class_id:
            with transaction.atomic():
                # Lock the rows for the current npc_system to prevent race conditions
                last_class = (
                    NpcSystemRpgClass.objects.select_for_update()
                    .filter(npc_system=self.npc_system)
                    .order_by("-rpg_class_id")
                    .first()
                )
                self.rpg_class_id = (last_class.rpg_class_id if last_class else 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a human-readable string representation of the RPG Class.

        The format includes the NPC system name, the designated table header for
        RPG classes from that system, and the class's value.

        Returns:
            str: A descriptive string for the instance.
        """
        return f"{self.npc_system.npc_system_name} - {self.npc_system.rpg_class_table_header}: {self.value}"
