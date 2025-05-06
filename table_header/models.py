from django.db import models
from npc_system.models import NpcSystem
from django.utils.translation import gettext_lazy as _
from table_group.models import TableGroup


# Create your models here.
class TableHeader(models.Model):
    npc_system = models.ForeignKey(
        "npc_system.NpcSystem",
        on_delete=models.CASCADE,
        related_name="table_headers",  # More intuitive related_name
        help_text="The NPC system this table header belongs to.",
    )
    table_group = models.ForeignKey(
        TableGroup,
        on_delete=models.CASCADE,  # Or models.PROTECT, models.SET_NULL depending on desired behavior
        related_name="sub_groups",  # Changed related_name to avoid clashes and be more descriptive
        help_text="The parent character group this sub-group belongs to.",
    )  # Consider if "sub_groups" is the best related_name from TableGroup to TableHeader. "table_headers" might also fit.
    name = models.CharField(
        max_length=50,
        help_text="The name of the table header (e.g., 'Combat', 'Magic', etc.).",
    )
    description = models.TextField(
        blank=True,
        help_text="A description of the table header.",
    )
    report_display_heading = models.CharField(
        max_length=50,
        blank=True,
        help_text="The heading to display in reports for this table header.",
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="The order in which this table header should be displayed.",
    )
    number_of_rolls = models.PositiveIntegerField(
        default=1,
        help_text="The number of rolls to make when using this table header.",
    )
    roll_die_type = models.CharField(
        max_length=50,
        blank=True,
        help_text="The type of roll to make when using this table header (e.g., '1d6', '2d10').",
    )
    roll_mod = models.IntegerField(
        default=0,
        help_text="The modifier to apply to the roll when using this table header.",
    )
    random_gen_inclusision_level = models.PositiveSmallIntegerField(
        _("Inclusion Level"),
        choices=[
            (1, "Full Only"),
            (2, "Medium"),
            (3, "Quick"),
        ],
        default=2,
        help_text="The inclusion level for this table header.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when this table header was created.",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="The date and time when this table header was last updated.",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Table Header"
        verbose_name_plural = "Table Headers"
        ordering = ["npc_system", "table_group", "display_order"]
