# Generated by Django 5.0.7 on 2024-07-16 10:46

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("newslist", "0001_initial"),
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
