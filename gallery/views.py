from django.shortcuts import render
from . import models
from django.views.generic import ListView


# Create your views here.
class GalleryView(ListView):
    model = models.Gallery
    context_object_name = "galleries"
    template_name = "gallery/galleries.html"
