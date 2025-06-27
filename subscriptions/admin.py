# subscriptions/admin.py

from django.contrib import admin
from subscriptions.models import Subscription
from simple_history.admin import SimpleHistoryAdmin


@admin.register(Subscription)
class SubscriptionAdmin(SimpleHistoryAdmin):
    # Use the correct field names from the Subscription model
    list_display = ("user", "subscription_type", "start_date", "end_date", "is_active")
    list_filter = ("subscription_type", "is_active")  # Use 'subscription_type'
    search_fields = ("user__email",)
    readonly_fields = ("start_date",)  # Use 'start_date'
