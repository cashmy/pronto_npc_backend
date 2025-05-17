# d:\Python-Django\pronto_npc_backend\users\models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings  # Import settings
from django.utils import timezone
from datetime import timedelta
import random
import string


# Create your models here.
class User(AbstractUser):
    # Add any additional fields you want to the user model here
    # For example, you can add a profile picture field
    # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    # is_active is already part of AbstractUser, no need to redefine unless changing default
    # is_active = models.BooleanField(default=True) # Already defaults to True in AbstractUser

    # Add the 'role' field if it's used in your admin.py fieldsets
    # Example:
    # ROLE_CHOICES = (
    #     ('admin', 'Admin'),
    #     ('editor', 'Editor'),
    #     ('viewer', 'Viewer'),
    # )
    # role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer')

    def __str__(self):
        # Using email might be more unique/useful than username if username isn't required
        return str(self.id)


# --- Add this model definition ---
class OneTimePassword(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user.email} - {self.code}"

    @staticmethod
    def generate_otp(length=6):
        """Generates a random OTP code."""
        characters = string.digits
        otp = "".join(random.choice(characters) for _ in range(length))
        # Ensure uniqueness (though collision is unlikely with short expiry)
        while OneTimePassword.objects.filter(code=otp).exists():
            otp = "".join(random.choice(characters) for _ in range(length))
        return otp

    def is_expired(self):
        """Checks if the OTP has expired."""
        return timezone.now() > self.expires_at

    def save(self, *args, **kwargs):
        """Set expiration time before saving."""
        if (
            not self.pk and not self.expires_at
        ):  # Only set on creation if not already set
            # Set OTP expiry duration (e.g., 5 minutes)
            self.expires_at = timezone.now() + timedelta(minutes=5)
        super().save(*args, **kwargs)


# --- End of added model ---
