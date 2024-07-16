# Generated by Django 5.0.7 on 2024-07-16 15:24

import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newslist", "0011_alter_userreport_tags"),
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="BnTag",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("taggit.tag",),
        ),
        migrations.CreateModel(
            name="BnTaggedItem",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("taggit.taggeditem",),
        ),
        migrations.AlterField(
            model_name="userreport",
            name="content",
            field=models.TextField(blank=True, null=True, verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="news",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="newslist.BnTaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="userreport",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="newslist.BnTaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]