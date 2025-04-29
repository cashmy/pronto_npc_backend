# subscriptions/views.py

from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from subscriptions.models import Subscription
from subscriptions.serializers import SubscriptionSerializer


class SubscriptionMeView(generics.RetrieveAPIView):
    """
    Retrieves the subscription details for the currently authenticated user.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubscriptionSerializer

    def get_object(self):
        # Use try-except to handle cases where the user might not have a subscription yet
        try:
            # Access the subscription via the related name from the User model
            # (Django automatically creates 'subscription' related name for OneToOneField)
            return self.request.user.subscription
        except Subscription.DoesNotExist:
            # You might want to return a 404 or a default/empty response
            # depending on your application's logic. Raising DoesNotExist
            # will result in a 404 by default in RetrieveAPIView.
            raise Subscription.DoesNotExist


class SubscriptionUpgradeView(APIView):
    """
    Allows an authenticated user to change their subscription type.
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Expect 'subscription_type' in the request data now
        new_subscription_type = request.data.get("subscription_type")

        # Get allowed choices directly from the model definition
        allowed_types = [choice[0] for choice in Subscription.PLAN_CHOICES]

        if not new_subscription_type:
            return Response(
                {"detail": "Missing 'subscription_type' field."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if new_subscription_type not in allowed_types:
            return Response(
                {
                    "detail": f'Invalid subscription type. Choose from: {", ".join(allowed_types)}'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            subscription = request.user.subscription
        except Subscription.DoesNotExist:
            # Handle case where user might not have an existing subscription
            # Depending on logic, you might create one or return an error
            return Response(
                {"detail": "No active subscription found to upgrade."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Update the correct field on the model
        subscription.subscription_type = new_subscription_type

        # --- Optional: Add logic for start/end dates ---
        # You might want to update start_date or end_date here
        # based on your business logic when a plan changes.
        # For example:
        # from django.utils import timezone
        # from datetime import timedelta
        # subscription.start_date = timezone.now().date()
        # subscription.end_date = timezone.now().date() + timedelta(days=30) # Example: 30 day subscription
        # subscription.is_active = True # Ensure it's active
        # --- End Optional ---

        subscription.save()

        # Use the display name for the response message
        updated_type_display = subscription.get_subscription_type_display()
        return Response(
            {"detail": f"Subscription successfully changed to {updated_type_display}."}
        )
