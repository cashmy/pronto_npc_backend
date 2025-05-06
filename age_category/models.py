from django.db import models


# Create your models here.
class AgeCategory(models.Model):
    age_category_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.age_category_name

    class Meta:
        verbose_name = "Age Category"
        verbose_name_plural = "Age Categories"
        ordering = ["age_category_name"]
