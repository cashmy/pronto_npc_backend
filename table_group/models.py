from django.db import models
from django.db.models import Max
from npc_system.models import NpcSystem  # Import the NpcSystem model


# Create your models here.
class TableGroup(models.Model):
    npc_system = models.ForeignKey(
        NpcSystem,
        on_delete=models.CASCADE,
        related_name="table_groups",
        help_text="The NPC system this table group belongs to.",
    )
    name = models.CharField(
        max_length=50,
        help_text="The name of the table group (e.g., 'Combat', 'Magic', etc.).",
    )
    description = models.TextField(
        blank=True,
        help_text="A description of the table group.",
    )
    report_display_heading = models.CharField(
        max_length=50,
        blank=True,
        help_text="The heading to display in reports for this table group.",
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="The order in which this table group should be displayed.",
    )
    number_of_rolls = models.PositiveIntegerField(
        default=1,
        help_text="The number of rolls to make when using this table group. The number of times to use this group of tables.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when this table group was created.",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="The date and time when this table group was last updated.",
    )

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to set report_display_heading if it's not provided.
        And to auto-increment the display_order within the context of the Table Group.
        """
        # Check if report_display_heading is empty (None or '') and name has a value
        if not self.report_display_heading and self.name:
            self.report_display_heading = self.name

        if not self.display_order:
            max_order = TableGroup.objects.filter(npc_system=self.npc_system).aggregate(
                Max("display_order")
            )["display_order__max"]
            self.display_order = (max_order or 0) + 10

        super().save(*args, **kwargs)  # Call the "real" save() method

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Table Group"
        verbose_name_plural = "Table Groups"
        ordering = ["npc_system", "display_order"]
        unique_together = ("npc_system", "name")  # Ensure composite uniqueness
