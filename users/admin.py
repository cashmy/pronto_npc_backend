# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User, OneTimePassword
from simple_history.admin import SimpleHistoryAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin, SimpleHistoryAdmin):
    list_display = (
        "id",
        "email",
        "username",
        "is_active",
        "is_staff",
        # "role", # Removed 'role'
        "date_joined",
    )
    list_filter = ("is_active", "is_staff")  # Removed 'role'
    search_fields = ("email", "username")
    ordering = ("-date_joined",)
    # Remove 'role' from fieldsets as well
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {"fields": ("is_email_verified",)}),  # Removed 'role'
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (
            None,
            {"fields": ("email", "is_email_verified")},
        ),  # Ensure email is in add_fieldsets if needed
    )
    readonly_fields = ("last_login", "date_joined")


@admin.register(OneTimePassword)
class OneTimePasswordAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "code",
        "created_at",
        "expires_at",
    )  # Added expires_at for info
    search_fields = ("user__email", "code")
    readonly_fields = (
        "created_at",
        "expires_at",
        "user",
        "code",
    )  # Make most fields read-only
