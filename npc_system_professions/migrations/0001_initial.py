# Generated by Django 5.2 on 2025-04-28 22:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('npc_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NpcSystemProfession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession_id', models.PositiveIntegerField(blank=True, db_index=True, editable=False, help_text='Auto-incrementing ID within the context of the NPC system.', null=True)),
                ('value', models.CharField(help_text='The name of the profession (e.g., Blacksmith, Hunter, Innkeeper).', max_length=25)),
                ('npc_system', models.ForeignKey(help_text='The NPC system this profession belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='professions', to='npc_system.npcsystem')),
            ],
            options={
                'verbose_name': 'Profession',
                'verbose_name_plural': 'Professions',
                'ordering': ['npc_system', 'id'],
                'unique_together': {('npc_system', 'id')},
            },
        ),
    ]
