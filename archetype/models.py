from django.db import models


# Create your models here.
class Archetype(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    notes = models.TextField(blank=True, null=True)
    expansion = models.BooleanField(default=False)
    related_archetypes = models.TextField(
        blank=True,
        null=True,
        help_text="Comma-separated list of related archetypes.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.expansion and self.related_archetypes:
            self.expansion = True  # Set to True if related archetypes are provided
        super().save(*args, **kwargs)  # Call the "real" save() method

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Archetype"
        verbose_name_plural = "Archetypes"
        ordering = ["expansion", "name"]
