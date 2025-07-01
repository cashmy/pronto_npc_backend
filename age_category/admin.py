from django.contrib import admin
from .models import AgeCategory


@admin.register(AgeCategory)
class AgeCategoryAdmin(admin.ModelAdmin):
    """Admin configuration for the AgeCategory model."""

    list_display = ("age_category_name", "created_at", "updated_at")
    search_fields = ("age_category_name",)
