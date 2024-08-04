from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


# Create your models here.
class Event(models.Model):
    title = models.CharField(
        verbose_name="A small title for the event.", max_length=250
    )
    description = HTMLField(verbose_name="Description")
    date = models.DateField(verbose_name="Date of the occerence")
    time = models.TimeField(verbose_name="Time of incident.", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(
        populate_from="title",
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event", kwargs={"slug": self.slug})
