from django.db import models


# Create your models here.
class Genre(models.Model):
    """
    Represents a genre for non-player characters (NPCs).

    This model stores information about different genres that can be assigned
    to NPCs, such as fantasy, sci-fi, or horror. It includes a name,
    a description, optional notes, and an icon.
    """

    name = models.CharField(max_length=255)
    """The name of the genre."""
    description = models.TextField()
    """A detailed description of the genre."""
    notes = models.TextField(blank=True, null=True)
    """Optional internal notes about the genre."""
    icon = models.FileField(upload_to="genre_icons/", blank=True, null=True)
    """An icon representing the genre."""
    created_at = models.DateTimeField(auto_now_add=True)
    """The timestamp when the genre was created."""
    updated_at = models.DateTimeField(auto_now=True)
    """The timestamp when the genre was last updated."""

    def __str__(self):
        """
        Returns the string representation of the genre.

        Returns:
            str: The name of the genre.
        """
        return self.name

    class Meta:
        """Meta options for the Genre model."""

        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        ordering = ["name"]
