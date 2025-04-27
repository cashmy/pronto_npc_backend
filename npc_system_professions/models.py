from django.db import models
from django.db.models import Max
from npc_system.models import NpcSystem


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
        blank=True,
        null=True,
        help_text="Auto-incrementing ID within the context of the NPC system.",
    )
    value = models.CharField(
        max_length=25,
        help_text="The name of the profession (e.g., Blacksmith, Hunter, Innkeeper).",
    )

    def save(self, *args, **kwargs):
        """
        Override the save method to auto-increment the ID within the context of the NPC system.
        """
        if not self.profession_id:
            max_id = NpcSystemProfession.objects.filter(
                npc_system=self.npc_system
            ).aggregate(Max("profession_id"))["profession_id__max"]
            self.profession_id = (max_id or 0) + 1
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
