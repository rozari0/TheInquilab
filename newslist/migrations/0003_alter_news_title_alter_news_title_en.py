# Generated by Django 5.0.7 on 2024-07-16 10:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("newslist", "0002_news_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(
                max_length=1000, verbose_name="News title in Bangla"
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="title_en",
            field=models.CharField(max_length=1000, verbose_name="Title in English."),
        ),
    ]
