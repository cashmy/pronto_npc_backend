from django.contrib import admin
from .models import NpcSystemProfession


@admin.register(NpcSystemProfession)
class NpcSystemProfessionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the NpcSystemProfession model.
    """

    list_display = (
        "npc_system",
        "profession_id",
        "value",
    )  # Fields to display in the list view
    list_filter = ("npc_system",)  # Add filtering by npc_system
    search_fields = ("value",)  # Add search functionality for the value field

    # Do not include profession_id in readonly_fields or exclude
    def get_readonly_fields(self, request, obj=None):
        """
        Dynamically set readonly fields. Exclude profession_id completely.
        """
        readonly_fields = super().get_readonly_fields(request, obj)
        return readonly_fields  # Do not include profession_id here

    def get_fields(self, request, obj=None):
        """
        Dynamically control which fields are displayed in the form.
        """
        fields = super().get_fields(request, obj)
        return [
            field for field in fields if field != "profession_id"
        ]  # Exclude profession_id
