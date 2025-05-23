# Generated by Django 5.2 on 2025-04-28 22:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('alt_text', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Alt Text')),
                ('file_size', models.PositiveIntegerField()),
                ('mime_type', models.CharField(max_length=25, verbose_name='Mime Type')),
                ('image', models.ImageField(upload_to='images/')),
                ('image_type', models.CharField(choices=[('i', 'Image'), ('a', 'Avatar'), ('t', 'Token'), ('s', 'Sidebar')], default='i', help_text='Type of the image (e.g., regular image, avatar, token)', max_length=1, verbose_name='Image Type')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnails/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
