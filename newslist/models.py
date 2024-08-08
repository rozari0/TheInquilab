from django.db import models
from django.db.models.signals import pre_save
from taggit.managers import TaggableManager
from tinymce.models import HTMLField

from .bn_taggit import BnTaggedItem


# Create your models here.
class News(models.Model):
    title = models.CharField(verbose_name="News title", max_length=1000)
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
    approved = models.BooleanField(verbose_name="Is Approved By admin?: ", default=True)
    tags = TaggableManager(through=BnTaggedItem)

    class Meta:
        verbose_name_plural = "News"
        ordering = ["-id"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.archive_link


def news_pre_save(sender, instance, *args, **kwargs):
    if instance.archive_link == "" or instance.archive_link is None:
        instance.archive_link = f"https://web.archive.org/save/{instance.link}"


pre_save.connect(news_pre_save, sender=News)


class Martyr(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    short_description = HTMLField(verbose_name="Short Description of martyr")
    image = models.URLField(verbose_name="Image of the martyr")
    birth = models.DateField(verbose_name="Date of birth", null=True, blank=True)
    death = models.DateField(verbose_name="Date of death", null=True, blank=True)
    approved = models.BooleanField(default=False, blank=True)

    class Meta:
        ordering = ["death", "name"]

    def __str__(self):
        return self.name


class LongDescription(models.Model):
    martyr_model = models.OneToOneField(
        Martyr, models.CASCADE, related_name="long_description"
    )
    description = HTMLField(verbose_name="Description of martyr")
