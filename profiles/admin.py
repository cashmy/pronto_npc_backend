# profiles/admin.py

from django.contrib import admin
from profiles.models import Profile
from simple_history.admin import SimpleHistoryAdmin


@admin.register(Profile)
class ProfileAdmin(SimpleHistoryAdmin):
    # Use fields that exist on the Profile model
    list_display = ("user", "referred_by_email", "date_of_birth")
    search_fields = ("user__email", "referred_by_email")  # Removed 'company'
    readonly_fields = ("user",)
