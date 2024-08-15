from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from slugify import slugify
from tinymce.models import HTMLField

# Create your models here.


def get_title_and_id(instance):
    return instance.title + "-" + str(instance.id)


class Event(models.Model):
    title = models.CharField(
        verbose_name="A small title for the event.", max_length=250
    )
    description = HTMLField(verbose_name="Description")
    read_more = HTMLField(verbose_name="Read More", null=True, blank=True)
    date = models.DateField(verbose_name="Date of the occerence")
    time = models.TimeField(verbose_name="Time of incident.", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from=get_title_and_id, unique=True, slugify=slugify)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event", kwargs={"slug": self.slug})
