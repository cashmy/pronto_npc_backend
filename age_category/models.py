"""Defines the data model for age categories."""

from django.db import models


class AgeCategory(models.Model):
    """Represents a distinct age category for a character (e.g., Child, Adult)."""

    age_category_name = models.CharField(max_length=50, unique=True)
    """The unique name of the age category (e.g., "Adult")."""
    description = models.TextField(blank=True, null=True)
    """An optional, detailed description of the age category."""
    created_at = models.DateTimeField(auto_now_add=True)
    """Timestamp of when the record was created."""
    updated_at = models.DateTimeField(auto_now=True)
    """Timestamp of the last update to the record."""

    def __str__(self):
        """Returns the string representation of the age category.

        Returns:
            str: The name of the age category.
        """
        return self.age_category_name

    class Meta:
        """Sets metadata options for the AgeCategory model."""
        verbose_name = "Age Category"
        verbose_name_plural = "Age Categories"
        ordering = ["age_category_name"]
