from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class News(models.Model):
    title = models.CharField(verbose_name="News title in Bangla", max_length=1000)
    title_en = models.CharField(verbose_name="Title in English.", max_length=1000)
    link = models.URLField(verbose_name="News URL")
    description = models.TextField(
        verbose_name="Description under 100 words.", null=True, blank=True
    )
    image = models.URLField(
        verbose_name="Image of incident if available", null=True, blank=True
    )
    archive_link = models.URLField(verbose_name="URL for archive.org", null=True)
    tags = TaggableManager()

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title_en + " | " + self.title
