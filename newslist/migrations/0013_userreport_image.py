# Generated by Django 5.0.7 on 2024-07-16 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newslist", "0012_bntag_bntaggeditem_alter_userreport_content_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userreport",
            name="image",
            field=models.URLField(
                blank=True, null=True, verbose_name="Image of incident if available"
            ),
        ),
    ]