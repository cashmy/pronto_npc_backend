# referrals/admin.py

from django.contrib import admin
from referrals.models import Referral  # Profile model is no longer needed here directly


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ("id", "referred_by", "code", "created_at", "total_signups")
    search_fields = ("referred_by__email", "code")
    readonly_fields = ("code", "created_at")

    def total_signups(self, obj):
        # obj is a Referral instance. Use the new model property.
        return obj.referred_user_count

    total_signups.short_description = "Total Referred Users"
