from random import choices
from string import ascii_letters

from autoslug import AutoSlugField
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from slugify import slugify
from tinymce.models import HTMLField


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=1000, help_text="Enter the title of the news.")
    link = models.URLField(
        help_text="Provide the link to the original news article.", max_length=2009
    )
    archive_link = models.URLField(
        null=True,
        blank=True,
        help_text="Optional: Provide a link to the archived version of the news.",
        max_length=2009,
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text="Optional: Enter a brief description of the news.",
    )
    image = models.URLField(
        null=True,
        blank=True,
        help_text="Optional: Provide a URL to an image related to the news.",
    )
    is_killed = models.BooleanField(
        default=False,
        blank=True,
        help_text="Check this box if the news relates to a fatal incident.",
    )
    approved = models.BooleanField(
        help_text="Indicate whether the news is approved by an admin.", default=False
    )
    published = models.DateField(
        null=True,
        blank=True,
        help_text="Optional: Enter the date when the news was published.",
    )

    class Meta:
        verbose_name_plural = "News"
        ordering = ["-published", "-id"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.archive_link


def news_pre_save(sender, instance, *args, **kwargs):
    if instance.archive_link == "" or instance.archive_link is None:
        instance.archive_link = f"https://web.archive.org/web/0/{instance.link}"


pre_save.connect(news_pre_save, sender=News)


def get_title_and_id(instance):
    return instance.name + "-" + "".join(choices(ascii_letters, k=3))


class Martyr(models.Model):
    name = models.CharField(
        max_length=100, help_text="Enter the full name of the martyr."
    )
    short_description = HTMLField(
        help_text="Provide a brief description of the martyr's life and legacy."
    )
    image = models.URLField(
        help_text="Provide a URL to an image of the martyr.",
        default="https://i.ibb.co/v3Bbnf5/gray-photo-placeholder.jpg",
    )
    birth = models.DateField(
        null=True, blank=True, help_text="Optional: Enter the birth date of the martyr."
    )
    death = models.DateField(
        null=True, blank=True, help_text="Optional: Enter the death date of the martyr."
    )
    approved = models.BooleanField(
        default=False,
        blank=True,
        help_text="Indicate whether the martyr's information is approved by an admin.",
    )
    slug = AutoSlugField(populate_from=get_title_and_id, unique=True, slugify=slugify)

    class Meta:
        ordering = ["death", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("martyr", args=[self.slug])


class LongDescription(models.Model):
    martyr_model = models.OneToOneField(
        Martyr, models.CASCADE, related_name="long_description"
    )
    description = HTMLField(verbose_name="Description of martyr")
