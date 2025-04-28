from django.db import models, transaction
from npc_system.models import NpcSystem
from django.utils.translation import gettext_lazy as _


class NpcSystemRace(models.Model):
    """
    Represents a race entry in the NPC system.
    """

    npc_system = models.ForeignKey(
        NpcSystem,
        on_delete=models.CASCADE,
        related_name="races",
        help_text="The NPC system this race belongs to.",
    )
    race_id = models.PositiveIntegerField(
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
    value = models.CharField(
        max_length=25,
        help_text="The name of the race (e.g., Human, Elf, Dwarf).",
    )

    def save(self, *args, **kwargs):
        """
        Override the save method to ensure race_id is unique and sequential context of the NPC system.
        Uses a transaction and select_for_update to prevent race conditions.
        """
        if not self.race_id:
            with transaction.atomic():  # Start a transaction
                # Lock the rows for the current npc_system to prevent race conditions
                last_race = (
                    NpcSystemRace.objects.select_for_update()
                    .filter(npc_system=self.npc_system)
                    .order_by("-race_id")
                    .first()
                )
                self.race_id = (last_race.race_id if last_race else 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the Race instance.
        Includes the NpcSystem name, race_table_header, and the race value.
        """
        return f"{self.npc_system.npc_system_name} - {self.npc_system.race_table_header}: {self.value}"

    class Meta:
        verbose_name = "Race"
        verbose_name_plural = "Races"
        ordering = ["npc_system", "id"]
        unique_together = ("npc_system", "id")  # Ensure composite uniqueness
