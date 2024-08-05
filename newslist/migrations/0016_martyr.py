# Generated by Django 5.0.7 on 2024-08-05 15:00

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newslist", "0015_alter_news_archive_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="Martyr",
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
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "description",
                    tinymce.models.HTMLField(verbose_name="Description of martyr"),
                ),
                ("image", models.URLField(verbose_name="Image of the martyr")),
            ],
        ),
    ]
