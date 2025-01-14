# Generated by Django 5.0.7 on 2024-08-05 15:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("newslist", "0016_martyr"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="martyr",
            options={"ordering": ["death", "name"]},
        ),
        migrations.AddField(
            model_name="martyr",
            name="death",
            field=models.DateField(blank=True, null=True, verbose_name="Date of death"),
        ),
    ]
