import os  # Needed for file deletion in the fixed delete method

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _  # <-- Import added here


# Create your models here.
class Image(models.Model):
    # Define choices for image_type
    class ImageType(models.TextChoices):
        IMAGE = "i", _("Image")
        AVATAR = "a", _("Avatar")
        TOKEN = "t", _("Token")
        SIDEBAR = "s", _("Sidebar")
        # Note: 'b' for thumbnail seems redundant if you have a separate field for it
        # THUMBNAIL = 'b', _('Thumbnail')

    file_name = models.CharField(max_length=255)
    alt_text = models.CharField(
        _("Alt Text"), max_length=50, blank=True, null=True, default=""
    )
    file_size = models.PositiveIntegerField()
    mime_type = models.CharField(_("Mime Type"), max_length=25)
    image = models.ImageField(upload_to="images/")  # Replaces the file_url field
    image_type = models.CharField(
        _("Image Type"),
        max_length=1,
        choices=ImageType.choices,
        default=ImageType.IMAGE,
        help_text=_("Type of the image (e.g., regular image, avatar, token)"),
    )
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="images",
        blank=True,
        null=True,  # If null, then the image is a system image
    )

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        # More robust __str__ method
        if self.alt_text:
            return self.alt_text
        elif self.file_name:
            return self.file_name
        else:
            return f"Image {self.pk}"

    def delete(self, *args, **kwargs):
        # Delete the main image file if it exists
        if self.image:
            # Check if the file exists before trying to delete
            if hasattr(self.image, "path") and os.path.exists(self.image.path):
                self.image.delete(
                    save=False
                )  # save=False prevents saving the model again

        # Delete the thumbnail file if it exists
        if self.thumbnail:
            # Check if the file exists before trying to delete
            if hasattr(self.thumbnail, "path") and os.path.exists(self.thumbnail.path):
                self.thumbnail.delete(save=False)

        super().delete(*args, **kwargs)  # Call the parent delete method
