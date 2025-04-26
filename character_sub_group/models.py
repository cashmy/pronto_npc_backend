# d:\Python-Django\pronto_npc_backend\character_sub_group\models.py
from django.db import models

# No need to import NpcSystem directly here anymore
from character_group.models import CharacterGroup  # Import the CharacterGroup


class CharacterSubGroup(models.Model):
    """
    Represents a specific sub-division within a CharacterGroup.
    Inherits the NpcSystem implicitly through its parent CharacterGroup.
    """

    character_group = models.ForeignKey(
        CharacterGroup,
        on_delete=models.CASCADE,  # Or models.PROTECT, models.SET_NULL depending on desired behavior
        related_name="sub_groups",  # Changed related_name to avoid clashes and be more descriptive
        help_text="The parent character group this sub-group belongs to.",
    )
    character_sub_group_name = models.CharField(
        max_length=75,
        help_text="The primary name of the character sub-group.",  # Updated help text
    )
    character_sub_group_short_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        help_text="An optional short name or abbreviation for the character sub-group.",  # Updated help text
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="An optional description providing more details about the character sub-group's purpose.",  # Updated help text
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Property to easily access the NpcSystem via the CharacterGroup
    @property
    def npc_system(self):
        return self.character_group.npc_system

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to set character_sub_group_short_name
        if it's not provided.
        """
        # Check if sub_group_short_name is empty (None or '') and sub_group_name has a value
        if (
            not self.character_sub_group_short_name and self.character_sub_group_name
        ):  # Corrected field names
            # Take the first 25 characters of the sub-group name
            self.character_sub_group_short_name = self.character_sub_group_name[
                :25
            ]  # Corrected field names
        super().save(*args, **kwargs)  # Call the "real" save() method

    def __str__(self):
        """
        Returns a string representation of the CharacterSubGroup instance.
        """
        # Use the short name if available, otherwise the full name
        display_name = (
            self.character_sub_group_short_name
            if self.character_sub_group_short_name
            else self.character_sub_group_name
        )
        # Access npc_system via character_group and use group's display name
        group_display_name = (
            self.character_group.character_group_short_name
            if self.character_group.character_group_short_name
            else self.character_group.character_group_name
        )
        # Construct a more hierarchical string representation
        return f"{self.npc_system.npc_system_name} / {group_display_name} / {display_name}"  # Improved string representation

    class Meta:
        # Optional: Add constraints like uniqueness if needed
        # Ensure a sub-group name is unique within its parent group
        # unique_together = ('character_group', 'character_sub_group_name')
        verbose_name = "Character Sub Group"
        verbose_name_plural = "Character Sub Groups"
        # Ordering now reflects the hierarchy correctly
        ordering = [
            "character_group__npc_system",
            "character_group",
            "id",
        ]  # Updated ordering
