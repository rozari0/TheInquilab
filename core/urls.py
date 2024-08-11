from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("badmin96/", admin.site.urls),
    path("", include("newslist.urls")),
    path("", include("timeline.urls")),
    path("tinymce/", include("tinymce.urls")),
    path("galleries/", include("gallery.urls")),
    path("api/v1/", include("core.api")),
]
