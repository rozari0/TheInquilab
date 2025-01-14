from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("newslist", "0014_alter_news_options_alter_userreport_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="archive_link",
            field=models.URLField(
                blank=True, null=True, verbose_name="URL for archive.org"
            ),
        ),
    ]
