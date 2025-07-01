from django.db import models


# Create your models here.
class Archetype(models.Model):
    """Represents a character archetype, a primordial model of a person or personality.

    Archetypes are universal patterns or models from which other things of the same kind are
    copied or on which they are based. In the context of storytelling and character creation,
    they represent fundamental human motifs. This model stores the definition and
    characteristics of various archetypes.
    """

    name = models.CharField(max_length=255)
    """The unique name of the archetype (e.g., 'Hero', 'Mentor', 'Trickster')."""
    description = models.TextField()
    """A detailed description of the archetype's characteristics, motivations, and role."""
    notes = models.TextField(blank=True, null=True)
    """Optional private notes or additional details about the archetype."""
    expansion = models.BooleanField(default=False)
    """A boolean flag indicating if this is a more specific, 'expansion' archetype."""
    related_archetypes = models.TextField(
        blank=True,
        null=True,
        help_text="Comma-separated list of related archetypes.",
    )
    """A text field to list names of related archetypes, typically broader or narrower concepts."""
    created_at = models.DateTimeField(auto_now_add=True)
    """The timestamp when the archetype was first created."""
    updated_at = models.DateTimeField(auto_now=True)
    """The timestamp of the last update to the archetype."""

    def save(self, *args, **kwargs):
        """Custom save method to manage the 'expansion' flag.

        This method overrides the default save behavior to automatically set the
        `expansion` flag to True if `related_archetypes` are provided for a
        non-expansion archetype. This enforces the logic that an archetype with
        relations is considered an expansion of a more fundamental concept.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if not self.expansion and self.related_archetypes:
            self.expansion = True  # Set to True if related archetypes are provided
        super().save(*args, **kwargs)  # Call the "real" save() method

    def __str__(self):
        """Returns the string representation of the archetype.

        Returns:
            str: The name of the archetype.
        """
        return self.name

    class Meta:
        """Metadata options for the Archetype model."""

        verbose_name = "Archetype"
        verbose_name_plural = "Archetypes"
        ordering = ["expansion", "name"]
