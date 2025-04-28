from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # Add any additional fields you want to the user model here
    # For example, you can add a profile picture field
    # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
