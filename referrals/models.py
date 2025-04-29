# referrals/models.py

import uuid
from django.db import models
from users.models import User


class Referral(models.Model):
    code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    referred_by = models.ForeignKey(
        User, related_name="referrals", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.referred_by.email} -> {self.code}"
