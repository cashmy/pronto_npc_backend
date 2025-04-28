from django.db import models


# Create your models here.
class AgeCategory(models.Model):
    age_category_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.age_category_name
