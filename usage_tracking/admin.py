# d:\Python-Django\pronto_npc_backend\usage_tracking\admin.py
from django.contrib import admin
from .models import UsageTracking


@admin.register(UsageTracking)
class UsageTrackingAdmin(admin.ModelAdmin):
    list_display = (
        "user_email",
        "npc_systems_generated_count",
        "characters_generated_count",
        "custom_generators_created_count",
        "ai_interfaced_characters_count",
        "ai_image_generated_characters_count",
        "updated_at",
    )
    search_fields = ("user__email", "user__username")
    readonly_fields = (
        "created_at",
        "updated_at",
    )  # User should not be changed once set

    def user_email(self, obj):
        return obj.user.email

    user_email.short_description = "User Email"
    user_email.admin_order_field = "user__email"

    # If you want to allow editing counts directly in admin (be cautious with this)
    # list_editable = (
    #     'npc_systems_generated_count',
    #     'characters_generated_count',
    #     'custom_generators_created_count',
    #     'ai_interfaced_characters_count',
    #     'ai_image_generated_characters_count',
    # )

    fieldsets = (
        (None, {"fields": ("user",)}),
        (
            "Usage Counts",
            {
                "fields": (
                    "npc_systems_generated_count",
                    "characters_generated_count",
                    "custom_generators_created_count",
                    "ai_interfaced_characters_count",
                    "ai_image_generated_characters_count",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),  # Optional: make this section collapsible
            },
        ),
    )
