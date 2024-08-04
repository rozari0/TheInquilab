from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Gallery(models.Model):
    title = models.CharField(verbose_name="Title of the gallery", max_length=500)
    description = HTMLField(null=True, blank=True)


class Image(models.Model):
    gallery = models.ForeignKey(
        Gallery, on_delete=models.SET_NULL, null=True, related_name="image"
    )
    caption = models.CharField(verbose_name="Caption", max_length=500)
    link = models.URLField(verbose_name="Image url")


class Video(models.Model):
    gallery = models.ForeignKey(
        Gallery, on_delete=models.SET_NULL, null=True, related_name="video"
    )
    caption = models.CharField(verbose_name="Caption", max_length=500)
    link = models.URLField(verbose_name="Image url")
