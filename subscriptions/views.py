# subscriptions/views.py

from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from subscriptions.models import Subscription
from subscriptions.serializers import SubscriptionSerializer
from django.utils import timezone
from datetime import timedelta  # Needed for reactivation logic


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def subscription_deactivate_me(request):
    """
    Deactivates the subscription for the currently authenticated user.
    Sets is_active to False and updates the end_date to now.
    """
    if request.method == "POST":
        try:
            subscription = request.user.subscription
        except Subscription.DoesNotExist:
            return Response(
                {"detail": "Subscription not found for this user."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except AttributeError:
            return Response(
                {"detail": "User not authenticated."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if not subscription.is_active:
            return Response(
                {"detail": "Subscription is already inactive."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Check if the subscription type is 'basic'
        if (
            subscription.subscription_type == Subscription.PLAN_CHOICES[0][0]
        ):  # Assuming 'basic' is the first choice
            return Response(
                {"detail": "Basic subscriptions cannot be deactivated."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        subscription.is_active = False
        subscription.end_date = timezone.now().date()  # Set end_date to today
        subscription.save()

        serializer = SubscriptionSerializer(subscription)
        return Response(
            {
                "detail": "Subscription successfully deactivated.",
                "subscription": serializer.data,
            }
        )


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def subscription_reactivate_me(request):
    """
    Reactivates the subscription for the currently authenticated user,
    if their plan is not 'basic'.
    Sets is_active to True, updates start_date to now, and end_date to 12 months from now.
    """
    if request.method == "POST":
        try:
            subscription = request.user.subscription
        except Subscription.DoesNotExist:
            return Response(
                {"detail": "Subscription not found for this user."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except AttributeError:
            return Response(
                {"detail": "User not authenticated."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # Check if the subscription type is 'basic'
        if (
            subscription.subscription_type == Subscription.PLAN_CHOICES[0][0]
        ):  # Assuming 'basic' is the first choice
            return Response(
                {
                    "detail": "Basic subscriptions cannot be reactivated through this process."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if subscription.is_active:
            return Response(
                {"detail": "Subscription is already active."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        subscription.is_active = True
        subscription.start_date = timezone.now()  # Update start date
        subscription.end_date = timezone.now().date() + timedelta(
            days=365
        )  # Extend end date by 12 months
        subscription.save()

        serializer = SubscriptionSerializer(subscription)
        return Response(
            {
                "detail": "Subscription successfully reactivated.",
                "subscription": serializer.data,
            }
        )


@api_view(["PUT", "PATCH"])
@permission_classes([permissions.IsAdminUser])  # Admin only
def subscription_admin_update(request, pk):
    """
    Allows an admin to update (PUT) or partially update (PATCH) any subscription.
    Note: 'start_date' is auto_now_add and typically not updated.
    """
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = SubscriptionSerializer(subscription, data=request.data)
    elif request.method == "PATCH":
        serializer = SubscriptionSerializer(
            subscription, data=request.data, partial=True
        )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def subscription_me(request):
    """
    Retrieves the subscription details for the currently authenticated user.
    """
    if request.method == "GET":
        try:
            # Access the subscription via the related name from the User model
            # (Django automatically creates 'subscription' related name for OneToOneField)
            subscription = request.user.subscription
            serializer = SubscriptionSerializer(subscription)
            return Response(serializer.data)
        except Subscription.DoesNotExist:
            # You might want to return a 404 or a default/empty response
            # depending on your application's logic. Raising DoesNotExist
            # will result in a 404 by default in RetrieveAPIView.
            return Response(
                {"detail": "Subscription not found for this user."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except AttributeError:
            # This can happen if request.user is AnonymousUser, though IsAuthenticated should prevent this.
            return Response(
                {"detail": "User not authenticated."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def subscription_upgrade(request):
    """
    Allows an authenticated user to change their subscription type.
    """
    if request.method == "POST":
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
        except AttributeError:
            return Response(
                {"detail": "User not authenticated."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # Update the correct field on the model
        subscription.subscription_type = new_subscription_type

        # --- Optional: Add logic for start/end dates ---
        # You might want to update start_date or end_date here
        # based on your business logic when a plan changes.
        # For example:
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
