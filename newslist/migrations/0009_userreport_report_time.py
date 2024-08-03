# Generated by Django 5.0.7 on 2024-07-16 13:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("newslist", "0008_userreport_alter_news_is_killed"),
    ]

    operations = [
        migrations.AddField(
            model_name="userreport",
            name="report_time",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
