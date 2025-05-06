from django.db import models
from users.models import User


# Create your models here.
class Subscription(models.Model):
    PLAN_CHOICES = [
        ("basic", "Basic"),
        ("standard", "Standard"),
        ("premium", "Premium"),
        ("storyteller", "Storyteller"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_type = models.CharField(
        max_length=50, choices=PLAN_CHOICES
    )  # Use choices here
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_subscription_type_display()}"  # Use display method for choices
