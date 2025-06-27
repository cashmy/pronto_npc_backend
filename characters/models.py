from django.db import models
from django.conf import settings

# Import foreign key files here
from npc_system.models import NpcSystem
from character_group.models import CharacterGroup
from character_sub_group.models import CharacterSubGroup
from archetype.models import Archetype

# The following fields will be selected or randomly generated from other tables/options
# (e.g., age category, race, character group, character sub-group, archetype, first name, last name, gender, etc.)


# Create your models here.
class Character(models.Model):
    """
    Represents a character in the system.
    """

    first_name = models.CharField(
        max_length=100,
        help_text="The first name.",
    )
    last_name = models.CharField(
        max_length=100,
        help_text="The last name.",
    )
    alias = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="An optional alias or knick name for the character.",
    )
    # Foreign key to NpcSystem
    npc_system = models.ForeignKey(
        NpcSystem,
        on_delete=models.CASCADE,
        related_name="characters",
        help_text="The NPC system this character belongs to.",
    )
    # Foreign key to CharacterGroup
    character_group = models.ForeignKey(
        CharacterGroup,
        on_delete=models.CASCADE,
        related_name="characters",
        help_text="The character group this character belongs to.",
    )
    # Foreign key to CharacterSubGroup
    character_sub_group = models.ForeignKey(
        CharacterSubGroup,
        on_delete=models.CASCADE,
        related_name="characters",
        help_text="The character sub-group this character belongs to.",
    )
    # Foreign key to Archetype
    archetype = models.ForeignKey(
        Archetype,
        on_delete=models.SET_NULL,
        related_name="characters",
        help_text="The archetype this character represents.",
        blank=True,
        null=True,
    )

    age_category_description = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="An optional description of the character's age category.",
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        help_text="The age of the character.",
    )
    race = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="The race of the character.",
    )
    profession = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="The occupation or profession of the character.",
    )
    rpg_class = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="The rpg class, fighter, wizard, etc.",
    )
    gender = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text="The gender of the character.",
    )
    current_location = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="The current location of the character.",
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="An optional description providing more details about the character.",
    )
    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Any additional notes about the character.",
    )
    bulk_generated = models.BooleanField(
        default=False,
        help_text="Indicates if the character was bulk-generated.",
    )
    reviewed = models.BooleanField(
        default=False,
        help_text="Indicates if the character has been reviewed.",
    )
    ai_integration_exists = models.BooleanField(
        default=False,
        help_text="Indicates if AI integration exists for this character.",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,  # If null, then the system is global
        related_name="characters",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the Character instance.
        """
        # Use the first name and last name for the string representation
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"
        ordering = ["npc_system", "id"]  # Default ordering
