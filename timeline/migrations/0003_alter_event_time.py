# Generated by Django 5.0.7 on 2024-08-02 23:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "timeline",
            "0002_event_time_alter_event_date_alter_event_description_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="time",
            field=models.TimeField(
                blank=True, null=True, verbose_name="Time of incident."
            ),
        ),
    ]
