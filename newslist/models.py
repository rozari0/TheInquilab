from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

from .bn_taggit import BnTaggedItem
from django.db.models.signals import pre_save


# Create your models here.
class News(models.Model):
    title = models.CharField(verbose_name="News title in Bangla", max_length=1000)
    title_en = models.CharField(verbose_name="Title in English.", max_length=1000)
    link = models.URLField(verbose_name="News URL")
    archive_link = models.URLField(
        verbose_name="URL for archive.org", null=True, blank=True
    )
    description = models.TextField(
        verbose_name="Description under 100 words.", null=True, blank=True
    )
    image = models.URLField(
        verbose_name="Image of incident if available", null=True, blank=True
    )
    is_killed = models.BooleanField(
        default=False,
        blank=True,
        verbose_name="Is someone has been unalived in this news?: ",
    )
    tags = TaggableManager(through=BnTaggedItem)

    class Meta:
        verbose_name_plural = "News"
        ordering = ["-id"]

    def __str__(self):
        return self.title_en + " | " + self.title

    def get_absolute_url(self):
        return self.archive_link


def news_pre_save(sender, instance, *args, **kwargs):
    if instance.archive_link == "" or instance.archive_link is None:
        instance.archive_link = f"https://web.archive.org/save/{instance.link}"


pre_save.connect(news_pre_save, sender=News)


class UserReport(models.Model):
    title = models.CharField(verbose_name="Title", max_length=1000)
    location = models.CharField(
        verbose_name="Your Location (X University)", null=True, max_length=100
    )
    image = models.URLField(
        verbose_name="Image of incident if available", null=True, blank=True
    )
    content = models.TextField(verbose_name="Description", blank=True, null=True)
    approved = models.BooleanField(default=False, blank=True)
    report_time = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True, through=BnTaggedItem)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title
