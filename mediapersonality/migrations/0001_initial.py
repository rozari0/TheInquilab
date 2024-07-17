# Generated by Django 5.0.7 on 2024-07-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Personality",
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
                    "name",
                    models.CharField(max_length=100, verbose_name="Person's Name"),
                ),
                (
                    "side",
                    models.CharField(
                        choices=[
                            ("FAVOR", "In Favor"),
                            ("AGAINST", "Opposed"),
                            ("COWARD", "Hasn't shared their view"),
                        ],
                        max_length=10,
                        verbose_name="Stand on this Protest",
                    ),
                ),
                (
                    "cause",
                    models.TextField(
                        blank=True, null=True, verbose_name="What did they do?"
                    ),
                ),
            ],
        ),
    ]
