# referrals/models.py

import uuid
from django.db import models
from users.models import User
from profiles.models import Profile  # Import the Profile model


class Referral(models.Model):
    code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    referred_by = models.ForeignKey(
        User, related_name="referrals", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.referred_by.email} -> {self.code}"

    @property
    def referred_user_count(self):
        """
        Calculates the number of users who were referred by the owner of this referral code.
        This is determined by counting Profile instances where referred_by_email
        matches the email of the user who made this referral.
        """
        return Profile.objects.filter(referred_by_email=self.referred_by.email).count()
