from django.db import models
from django.db.models import Max
from npc_system.models import NpcSystem


class NpcSystemRpgClass(models.Model):
    """
    Represents a race entry in the NPC system.
    """

    npc_system = models.ForeignKey(
        NpcSystem,
        on_delete=models.CASCADE,
        related_name="rpg_classes",
        help_text="The NPC system this RPG Class belongs to.",
    )
    rpg_class_id = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Auto-incrementing ID within the context of the NPC system.",
    )
    value = models.CharField(
        max_length=25,
        help_text="The name of the class (e.g., Warrior, Thief, Mage).",
    )

    def save(self, *args, **kwargs):
        """
        Override the save method to auto-increment the ID within the context of the NPC system.
        """
        if not self.rpg_class_id:
            max_id = NpcSystemRpgClass.objects.filter(
                npc_system=self.npc_system
            ).aggregate(Max("rpg_class_id"))["rpg_class_id__max"]
            self.rpg_class_id = (max_id or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the Race instance.
        Includes the NpcSystem name, rpg_class_table_header, and the rpg class value.
        """
        return f"{self.npc_system.npc_system_name} - {self.npc_system.rpg_class_table_header}: {self.value}"

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ["npc_system", "id"]
        unique_together = ("npc_system", "id")  # Ensure composite uniqueness
