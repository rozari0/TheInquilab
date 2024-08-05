from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView

from . import models


# Create your views here.
class GalleryView(ListView):
    model = models.Gallery
    context_object_name = "galleries"
    template_name = "gallery/galleries.html"

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
