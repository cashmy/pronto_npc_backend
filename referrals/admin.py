# referrals/admin.py

from django.contrib import admin
from referrals.models import Referral


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ("id", "referred_by", "code", "created_at", "total_signups")
    search_fields = ("referred_by__email", "code")
    readonly_fields = ("code", "created_at")

    def total_signups(self, obj):
        # Optional: if you track referred users in Profile model
        return obj.referred_by.referred_users.count()

    total_signups.short_description = "Total Referred Users"
