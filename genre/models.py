from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    notes = models.TextField(blank=True, null=True)
    icon = models.FileField(upload_to="genre_icons/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        ordering = ["name"]
