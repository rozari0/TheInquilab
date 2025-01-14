# Generated by Django 5.0.7 on 2024-08-05 21:24

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("newslist", "0019_alter_martyr_short_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="LongDescription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    tinymce.models.HTMLField(verbose_name="Description of martyr"),
                ),
                (
                    "martyr_model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="long_description",
                        to="newslist.martyr",
                    ),
                ),
            ],
        ),
    ]
