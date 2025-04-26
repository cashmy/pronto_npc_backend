from django.db import models
from npc_system.models import NpcSystem


# Create your models here.
class CharacterGroup(models.Model):
    """
    Represents a logical grouping of related systems.
    """

    npc_system = models.ForeignKey(
        NpcSystem,
        on_delete=models.CASCADE,  # Or models.PROTECT, models.SET_NULL depending on desired behavior
        related_name="groups",
    )
    character_group_name = models.CharField(
        max_length=75,
        help_text="The primary name of the character group for this NPC system.",
    )
    character_group_short_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        help_text="An optional short name or abbreviation for the character group.",
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="An optional description providing more details about the character group's purpose.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to set character_group_short_name
        if it's not provided.
        """
        # Check if short_name is empty (None or '') and group_name has a value
        if not self.character_group_short_name and self.character_group_name:
            # Take the first 15 characters of the group name
            self.character_group_short_name = self.character_group_name[:25]
        super().save(*args, **kwargs)  # Call the "real" save() method

    def __str__(self):
        """
        Returns a string representation of the CharacterGroup instance.
        """
        # Consider using the short name if it exists for a more concise representation
        display_name = (
            self.character_group_short_name
            if self.character_group_short_name
            else self.character_group_name
        )
        return f"{self.npc_system.npc_system_name} - {display_name}"

    class Meta:
        # Optional: Add constraints like uniqueness if needed
        # unique_together = ('npc_system', 'character_group_name')
        verbose_name = "Character Group"
        verbose_name_plural = "Character Groups"
        ordering = ["npc_system", "id"]  # Default ordering
