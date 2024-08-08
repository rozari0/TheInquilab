# Generated by Django 5.0.7 on 2024-08-07 05:32

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("timeline", "0003_alter_event_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="read_more",
            field=tinymce.models.HTMLField(
                blank=True, null=True, verbose_name="Description"
            ),
        ),
    ]