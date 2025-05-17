from django.db import models
from users.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    theme = models.CharField(
        max_length=50,
        choices=[("light", "Light"), ("dark", "Dark"), ("system", "System")],
        default="light",
    )
    referred_by_email = models.EmailField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Email of the user who referred you.",
    )
    discord_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Discord ID of the user, if applicable.",
    )
    location = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Location of the user, if applicable.",
    )
    # SAVE: For future use:
    # country_code = models.CharField(
    #     max_length=10,
    #     blank=True,
    #     null=True,
    #     help_text="Country code of the user, if applicable.",
    # )

    def __str__(self):
        return self.user.username
