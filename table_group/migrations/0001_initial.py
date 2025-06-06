# Generated by Django 5.2 on 2025-04-28 22:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('npc_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="The name of the table group (e.g., 'Combat', 'Magic', etc.).", max_length=50)),
                ('description', models.TextField(blank=True, help_text='A description of the table group.')),
                ('report_display_heading', models.CharField(blank=True, help_text='The heading to display in reports for this table group.', max_length=50)),
                ('display_order', models.PositiveIntegerField(default=0, help_text='The order in which this table group should be displayed.')),
                ('number_of_rolls', models.PositiveIntegerField(default=1, help_text='The number of rolls to make when using this table group. The number of times to use this group of tables.')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when this table group was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The date and time when this table group was last updated.')),
                ('npc_system', models.ForeignKey(help_text='The NPC system this table group belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='table_groups', to='npc_system.npcsystem')),
            ],
            options={
                'verbose_name': 'Table Group',
                'verbose_name_plural': 'Table Groups',
                'ordering': ['npc_system', 'display_order'],
                'unique_together': {('npc_system', 'name')},
            },
        ),
    ]
