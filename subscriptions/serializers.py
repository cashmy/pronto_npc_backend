# subscriptions/serializers.py

from rest_framework import serializers
from subscriptions.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ("subscription_type", "start_date", "end_date", "is_active")
        read_only_fields = ("start_date",)
