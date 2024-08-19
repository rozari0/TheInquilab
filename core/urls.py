from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from newslist.sitemap import sitemaps

urlpatterns = [
    path("badmin96/", admin.site.urls),
    path("", include("newslist.urls")),
    path("", include("timeline.urls")),
    path("tinymce/", include("tinymce.urls")),
    path("galleries/", include("gallery.urls")),
    path("api/v1/", include("core.api")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
