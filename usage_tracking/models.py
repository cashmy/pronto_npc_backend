# d:\Python-Django\pronto_npc_backend\usage_tracking\models.py
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class UsageTracking(models.Model):
    """
    Tracks usage metrics for a user, linked to their account.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="usage_metrics",
        verbose_name=_("User"),
    )

    npc_systems_generated_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("NPC Systems Generated"),
        help_text=_("Number of NPC systems generated by the user."),
    )
    characters_generated_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Characters Generated"),
        help_text=_("Number of characters generated by the user."),
    )
    custom_generators_created_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Custom Generators Created"),
        help_text=_("Number of custom random table generators created by the user."),
    )
    custom_generator_tables_created_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Custom Generators Created"),
        help_text=_("Number of custom random table generators created by the user."),
    )
    character_avatars_uploaded_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Character Avatars Uploaded"),
        help_text=_("Number of character avatars uploaded by the user."),
    )
    character_tokens_uploaded_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Character Avatars Uploaded"),
        help_text=_("Number of character avatars uploaded by the user."),
    )
    ai_interfaced_characters_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("AI Interfaced Characters"),
        help_text=_(
            "Number of characters for whom an AI interface/integration has been activated."
        ),
    )
    ai_image_generated_characters_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("AI Image Generated for Characters"),
        help_text=_("Number of characters for whom an AI image has been generated."),
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("User Usage")
        verbose_name_plural = _("User Usages")
        ordering = ["user__email"]  # Optional: for ordering in admin or queries

    def __str__(self):
        return f"Usage metrics for {self.user.email or self.user.username}"

    # Potentially add methods here to check against subscription limits
    # For example:
    # def can_generate_npc_system(self):
    #     if hasattr(self.user, 'subscription') and self.user.subscription:
    #         limit = self.user.subscription.get_limit_for('npc_systems') # Hypothetical method
    #         return self.npc_systems_generated_count < limit
    #     return True # Or False, depending on default behavior without subscription

    # def increment_npc_systems_count(self):
    #     self.npc_systems_generated_count += 1
    #     self.save(update_fields=['npc_systems_generated_count', 'updated_at'])

    # def increment_characters_count(self):
    #     self.characters_generated_count += 1
    #     self.save(update_fields=['characters_generated_count', 'updated_at'])

    # ... and so on for other counters
