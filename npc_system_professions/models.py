"""
Defines the data model for Professions within the NPC system.

This module contains the `NpcSystemProfession` model, which represents a specific
profession (e.g., Blacksmith, Hunter) that can be assigned to an NPC within a
particular game system.
"""

from django.db import models, transaction

from npc_system.models import NpcSystem


class NpcSystemProfession(models.Model):
    """
    Represents a Profession within a specific NPC system.

    A Profession is an occupation that an NPC can have, such as "Blacksmith",
    "Hunter", or "Innkeeper". Each profession is tied to a specific
    :class:`~npc_system.models.NpcSystem`, ensuring that professions are unique
    and managed within the context of their game system.
    """

    npc_system = models.ForeignKey(
        NpcSystem,
        on_delete=models.CASCADE,
        related_name="professions",
        help_text="The NPC system this profession belongs to.",
    )
    """A reference to the :class:`~npc_system.models.NpcSystem` this profession belongs to."""

    profession_id = models.PositiveIntegerField(
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
        help_text="The name of the profession (e.g., Blacksmith, Hunter, Innkeeper).",
    )
    """The name of the profession (e.g., "Blacksmith")."""

    class Meta:
        """Meta options for the NpcSystemProfession model."""

        verbose_name = "Profession"
        verbose_name_plural = "Professions"
        ordering = ["npc_system", "id"]
        # Ensures profession_id is unique within the scope of an npc_system.
        unique_together = ("npc_system", "profession_id")

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to manage `profession_id`.

        If `profession_id` is not already set, this method assigns a new,
        sequential ID within the context of the parent `npc_system`. It uses a
        database transaction with `select_for_update` to lock the relevant
        rows, preventing race conditions when multiple professions are created
        concurrently for the same system.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if not self.profession_id:
            with transaction.atomic():
                # Lock the rows for the current npc_system to prevent race conditions
                last_profession = (
                    NpcSystemProfession.objects.select_for_update()
                    .filter(npc_system=self.npc_system)
                    .order_by("-profession_id")
                    .first()
                )
                self.profession_id = (
                    last_profession.profession_id if last_profession else 0
                ) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a human-readable string representation of the Profession.

        The format includes the NPC system name, the designated table header for
        professions from that system, and the profession's value.

        Returns:
            str: A descriptive string for the instance.
        """
        return f"{self.npc_system.npc_system_name} - {self.npc_system.profession_table_header}: {self.value}"
