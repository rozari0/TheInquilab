# Generated by Django 5.0.7 on 2024-07-16 10:45

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("title", models.TextField(verbose_name="News title in Bangla")),
                ("title_en", models.TextField(verbose_name="Title in English.")),
                ("link", models.URLField(verbose_name="News URL")),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="Description under 100 words.",
                    ),
                ),
            ],
        ),
    ]
