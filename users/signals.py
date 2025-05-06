from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings  # To get the custom User model
from django.utils import timezone
from datetime import timedelta

from profiles.models import Profile
from subscriptions.models import Subscription

# Import Referral model if you intend to create a default referral record for the new user,
# though referral processing (linking to a referrer) is often handled during registration.
# from referrals.models import Referral

# Get the User model dynamically
User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_user_related_records(sender, instance, created, **kwargs):
    """
    Signal handler to create related records when a new User is created.
    - Creates a Profile for the new user.
    - Creates a default Subscription for the new user.
    """
    if created:
        # Create a Profile for the new user
        Profile.objects.create(user=instance)

        # Create a default Subscription for the new user
        # You might want to adjust the default subscription type and duration
        default_subscription_type = Subscription.PLAN_CHOICES[0][0]  # e.g., 'basic'
        start_date = timezone.now().date()
        # Example: Default 'basic' plan is free and effectively doesn't expire,
        # or has a very long duration. Or set a trial period.
        # For a trial, you might do: end_date = start_date + timedelta(days=30)
        # For a "free forever" type, a very distant date or a specific flag might be used.
        # Let's assume a long duration for a basic/free tier for now.
        end_date = start_date + timedelta(days=365 * 10)  # Example: 10 years

        Subscription.objects.create(
            user=instance,
            subscription_type=default_subscription_type,
            start_date=start_date,
            end_date=end_date,
            is_active=True,
        )

        # If you also want to create a Referral record for the user themselves
        # (so they can start referring others), you could do it here.
        # However, linking a new user to an *existing* referrer based on a code
        # is usually handled in the registration view/serializer.
        # Example: Referral.objects.create(referred_by=instance, ...)
