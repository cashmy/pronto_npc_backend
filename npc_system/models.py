from django.conf import settings
from django.db import models
from genre.models import Genre


# Create your models here.
class NpcSystem(models.Model):
    npc_system_name = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="The genre of the NPC system, e.g., Fantasy, Sci-Fi, etc.",
        default="",
    )
    standard_app_dsp = models.BooleanField(default=False)
    """ Indicates if the system has a standard front end view/modal for the add.edit operation
        If not then the system will display its tables in a generic table view for the add/edit operation
    """

    is_global = models.BooleanField(default=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,  # If null, then the system is global
        related_name="custom_systems",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.npc_system_name

    def is_visible_to(self, user):
        """
        Helper method to check if a system is visible to a given user.
        Global systems are visible to all users.
        User-specific systems are only visible to the owner.
        """
        return self.is_global or self.owner == user
