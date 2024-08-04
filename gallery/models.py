from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Gallery(models.Model):
    title = models.CharField(verbose_name="Title of the gallery", max_length=500)
    description = HTMLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "galleries"

    def __str__(self):
        return self.title


class Image(models.Model):
    gallery = models.ForeignKey(
        Gallery, on_delete=models.SET_NULL, null=True, related_name="image"
    )
    caption = models.CharField(verbose_name="Caption", max_length=500)
    link = models.URLField(verbose_name="Image url")

    def __str__(self):
        return self.caption[:50] if self.caption else self.id


class Video(models.Model):
    gallery = models.ForeignKey(
        Gallery, on_delete=models.SET_NULL, null=True, related_name="video"
    )
    caption = models.CharField(verbose_name="Caption", max_length=500)
    link = models.URLField(verbose_name="Image url")
