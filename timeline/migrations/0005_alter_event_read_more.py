# Generated by Django 5.0.7 on 2024-08-07 06:28

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("timeline", "0004_event_read_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="read_more",
            field=tinymce.models.HTMLField(
                blank=True, null=True, verbose_name="Read More"
            ),
        ),
    ]
