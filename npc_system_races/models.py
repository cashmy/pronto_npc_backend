from django.db import models, transaction
from npc_system.models import NpcSystem
from django.utils.translation import gettext_lazy as _


class NpcSystemRace(models.Model):
    """Represents a race within a specific NPC system.

    This model stores individual races (e.g., 'Human', 'Elf') and links them
    to a parent `NpcSystem`. It includes a custom `save` method to generate a
    unique, sequential `race_id` for each race within the context of its
    NPC system, ensuring that races are numbered starting from 1 for each system.

    """

    npc_system = models.ForeignKey(
        NpcSystem,
        on_delete=models.CASCADE,
        related_name="races",
        help_text="The NPC system this race belongs to.",

    )
    """The NPC system this race belongs to."""
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
    """A unique, sequential identifier for the race within its parent NpcSystem."""
    value = models.CharField(
        max_length=25,
        help_text="The name of the race (e.g., Human, Elf, Dwarf).",
    )
    """The name of the race (e.g., "Human", "Elf", "Dwarf")."""

    def save(self, *args, **kwargs):
        """Overrides the default save to assign a sequential `race_id`.

        This method ensures that each new race gets a `race_id` that is unique
        and sequential within its parent `NpcSystem`. It uses a database
        transaction and `select_for_update` to lock the relevant rows,
        preventing race conditions when multiple races for the same system are
        created concurrently. If the instance already has a `race_id`, this
        logic is skipped.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
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

    class Meta:
        """Sets metadata options for the NpcSystemRace model."""
        verbose_name = "Race"
        verbose_name_plural = "Races"
        ordering = ["npc_system", "id"]
        unique_together = ("npc_system", "race_id")  # Ensure composite uniqueness

    def __str__(self):
        """Returns a human-readable string representation of the race.

        Returns:
            str: A string combining the NPC system name, its race table header, and the race's value.
        """
        return f"{self.npc_system.npc_system_name} - {self.npc_system.race_table_header}: {self.value}"
