from django.db import models, transaction
from npc_system.models import NpcSystem
from django.utils.translation import gettext_lazy as _


class NpcSystemProfession(models.Model):
    """
    Represents a profession entry in the NPC system.
    """

    npc_system = models.ForeignKey(
        NpcSystem,
        on_delete=models.CASCADE,
        related_name="professions",
        help_text="The NPC system this profession belongs to.",
    )
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
    value = models.CharField(
        max_length=25,
        help_text="The name of the profession (e.g., Blacksmith, Hunter, Innkeeper).",
    )

    def save(self, *args, **kwargs):
        """
        Override the save method to ensure profession_id is unique and sequential context of the NPC system.
        Uses a transaction and select_for_update to prevent race conditions.
        """
        if not self.profession_id:
            with transaction.atomic():
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
        Returns a string representation of the Profession instance.
        Includes the NpcSystem name, profession_table_header, and the profession value.
        """
        return f"{self.npc_system.npc_system_name} - {self.npc_system.profession_table_header}: {self.value}"

    class Meta:
        verbose_name = "Profession"
        verbose_name_plural = "Professions"
        ordering = ["npc_system", "id"]
        unique_together = ("npc_system", "id")  # Ensure composite uniqueness
