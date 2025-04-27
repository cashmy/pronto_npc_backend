from django.db import models
from django.db.models import Max
from npc_system.models import NpcSystem


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
        blank=True,
        null=True,
        help_text="Auto-incrementing ID within the context of the NPC system.",
    )
    value = models.CharField(
        max_length=25,
        help_text="The name of the race (e.g., Human, Elf, Dwarf).",
    )

    def save(self, *args, **kwargs):
        """
        Override the save method to auto-increment the ID within the context of the NPC system.
        """
        if not self.race_id:
            # # Find the current max race_id for this parent
            # last_race = (
            #     NpcSystemRace.objects.filter(npc_system=self.npc_system)
            #     .order_by("-race_id")
            #     .first()
            # )
            # if last_race:
            #     self.race_id = last_race.race_id + 1
            # else:
            #     self.race_id = 1
            # if not self.race_id:
            # Get the maximum race_id for the current NPC system
            max_id = NpcSystemRace.objects.filter(npc_system=self.npc_system).aggregate(
                Max("race_id")
            )["race_id__max"]
            self.race_id = (max_id or 0) + 1
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
