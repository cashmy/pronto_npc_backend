from django.conf import settings
from django.db import models
from genre.models import Genre


# Create your models here.
class NpcSystem(models.Model):
    """Represents a core NPC generation system.

    This model acts as a container for all related settings and data for a
    specific NPC generation context, such as a particular tabletop RPG system
    or a unique world setting. It links to genres, owners, and defines
    thematic elements like table headers and color schemes.
    """
    npc_system_name = models.CharField(max_length=255)
    """The unique name of the NPC system."""
    description = models.TextField()
    """A detailed description of the NPC system."""
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="The genre of the NPC system, e.g., Fantasy, Sci-Fi, etc.",
        default=None,  # Changed from default=""
    )
    """The genre of the NPC system, e.g., Fantasy, Sci-Fi, etc."""
    npc_system_image = models.ImageField(
        upload_to="npc_systems/images/",
        blank=True,
        null=True,
        help_text="An image representing the NPC system",
    )
    """An image representing the NPC system."""
    npc_system_icon = models.ImageField(
        upload_to="npc_systems/icons/",
        blank=True,
        null=True,
        help_text="An icon representing the NPC system",
    )
    """An icon representing the NPC system."""
    npc_system_color = models.CharField(
        max_length=7,
        blank=True,
        null=True,
        help_text="A color code representing the NPC system, e.g., #FF5733",
    )
    """A color code representing the NPC system, e.g., '#FF5733'."""
    npc_system_color_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="A name for the color representing the NPC system, e.g., 'Fire Red'",
    )
    """A name for the color representing the NPC system, e.g., 'Fire Red'."""
    race_table_header = models.CharField(
        max_length=25,
        blank=False,
        null=False,
        help_text="The header for the race table",
        default="Race",
    )
    """The header for the race table."""

    profession_table_header = models.CharField(
        max_length=25,
        blank=False,
        null=False,
        help_text="The header for the profession table",
        default="Profession",
    )
    """The header for the profession table."""

    rpg_class_table_header = models.CharField(
        max_length=25,
        blank=False,
        null=False,
        help_text="The header for the RPG class table",
        default="Class",
    )
    """The header for the RPG class table."""

    standard_app_dsp = models.BooleanField(default=False)
    """Indicates if the system uses a standard frontend view/modal.

    If False, the system's tables may be displayed in a generic table view
    for add/edit operations.
    """

    is_global = models.BooleanField(default=False)
    """If True, this system is available to all users."""
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,  # If null, then the system is global
        related_name="custom_systems",
    )
    """The user who owns this system. If null, the system is global."""
    created_at = models.DateTimeField(auto_now_add=True)
    """Timestamp of when the record was created."""
    updated_at = models.DateTimeField(auto_now=True)
    """Timestamp of the last update to the record."""

    def __str__(self):
        """Returns the string representation of the NPC system.

        Returns:
            str: The name of the NPC system.
        """
        return self.npc_system_name

    def is_visible_to(self, user):
        """Checks if the system is visible to a given user.

        Global systems are visible to all authenticated users. User-specific
        systems are only visible to their owner.

        Args:
            user: The user instance to check visibility for.

        Returns:
            bool: True if the user can view the system, False otherwise.
        """
        return self.is_global or self.owner == user
