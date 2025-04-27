from django.db import models
from images.models import Image  # Import the Image model
from characters.models import Character  # Import the Character model


class CharacterImage(models.Model):
    """
    Represents an image associated with a character.
    """

    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        related_name="character_images",
        help_text="The character this image is associated with.",
    )
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name="character_images",
        help_text="The image associated with the character.",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the CharacterImage instance.
        """
        return f"{self.character.first_name} {self.character.last_name} ({self.character.race}) - {self.image.get_image_type_display()} - {self.image.file_name}"

    class Meta:
        verbose_name = "Character Image"
        verbose_name_plural = "Character Images"
        ordering = ["character", "id"]
