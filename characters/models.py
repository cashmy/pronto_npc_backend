from django.conf import settings
from django.db import models

from archetype.models import Archetype
from character_group.models import CharacterGroup
from character_sub_group.models import CharacterSubGroup

# Import foreign key files here
from npc_system.models import NpcSystem

# The following fields will be selected or randomly generated from other tables/options
# (e.g., age category, race, character group, character sub-group, archetype, first name, last name, gender, etc.)


# Create your models here.
class Character(models.Model):
    """
    Represents a character within a specific NPC system.

    This model stores all the details about a character, including their
    personal information (name, age, race, etc.), their role within the
    game world (profession, RPG class), and their relationships to other
    data structures like NPC systems, character groups, and archetypes.
    It also includes metadata for content management, such as review status
    and AI integration flags.
    """

    first_name = models.CharField(
        max_length=100,
        help_text="The first name.",
    )
    """The first name of the character."""
    last_name = models.CharField(
        max_length=100,
        help_text="The last name.",
    )
    """The last name of the character."""
    alias = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="An optional alias or knick name for the character.",
    )
    """An optional alias or nickname for the character."""
    # Foreign key to NpcSystem
    npc_system = models.ForeignKey(
        NpcSystem,
        on_delete=models.CASCADE,
        related_name="characters",
        help_text="The NPC system this character belongs to.",
    )
    """The NPC system this character belongs to."""
    # Foreign key to CharacterGroup
    character_group = models.ForeignKey(
        CharacterGroup,
        on_delete=models.CASCADE,
        related_name="characters",
        help_text="The character group this character belongs to.",
    )
    """The character group this character belongs to."""
    # Foreign key to CharacterSubGroup
    character_sub_group = models.ForeignKey(
        CharacterSubGroup,
        on_delete=models.CASCADE,
        related_name="characters",
        help_text="The character sub-group this character belongs to.",
    )
    """The character sub-group this character belongs to."""
    # Foreign key to Archetype
    archetype = models.ForeignKey(
        Archetype,
        on_delete=models.SET_NULL,
        related_name="characters",
        help_text="The archetype this character represents.",
        blank=True,
        null=True,
    )
    """The archetype this character represents."""

    age_category_description = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="An optional description of the character's age category.",
    )
    """An optional description of the character's age category (e.g., 'Young Adult', 'Elderly')."""
    age = models.IntegerField(
        blank=True,
        null=True,
        help_text="The age of the character.",
    )
    """The numerical age of the character."""
    race = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="The race of the character.",
    )
    """The race or species of the character."""
    profession = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="The occupation or profession of the character.",
    )
    """The occupation or profession of the character."""
    rpg_class = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="The rpg class, fighter, wizard, etc.",
    )
    """The RPG class of the character (e.g., 'Fighter', 'Wizard')."""
    gender = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text="The gender of the character.",
    )
    """The gender of the character."""
    current_location = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="The current location of the character.",
    )
    """The current known location of the character."""
    description = models.TextField(
        blank=True,
        null=True,
        help_text="An optional description providing more details about the character.",
    )
    """A detailed description of the character's appearance, personality, and background."""
    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Any additional notes about the character.",
    )
    """Private notes or metadata for the game master or system administrator."""
    bulk_generated = models.BooleanField(
        default=False,
        help_text="Indicates if the character was bulk-generated.",
    )
    """A flag indicating if the character was created as part of a bulk generation process."""
    reviewed = models.BooleanField(
        default=False,
        help_text="Indicates if the character has been reviewed.",
    )
    """A flag indicating if the character's details have been reviewed and approved."""
    ai_integration_exists = models.BooleanField(
        default=False,
        help_text="Indicates if AI integration exists for this character.",
    )
    """A flag indicating if an AI model or integration is associated with this character."""
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,  # If null, then the system is global
        related_name="characters",
    )
    """The user who owns this character. If null, the character is considered global."""
    created_at = models.DateTimeField(auto_now_add=True)
    """The timestamp when the character was created."""
    updated_at = models.DateTimeField(auto_now=True)
    """The timestamp when the character was last updated."""

    def __str__(self):
        """
        Return a string representation of the Character.

        Returns:
            str: The full name of the character.
        """
        # Use the first name and last name for the string representation
        return f"{self.first_name} {self.last_name}"

    class Meta:
        """Metadata options for the Character model."""

        verbose_name = "Character"
        verbose_name_plural = "Characters"
        ordering = ["npc_system", "id"]  # Default ordering
