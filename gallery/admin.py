from django.contrib import admin

from . import models

# Register your models here.


class VideoInline(admin.StackedInline):
    model = models.Video


class ImageInline(admin.StackedInline):
    model = models.Image


class GalleryAdmin(admin.ModelAdmin):
    inlines = [ImageInline, VideoInline]


admin.site.register(models.Gallery, GalleryAdmin)
