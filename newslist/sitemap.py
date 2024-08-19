from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from timeline.models import Event

from .models import Martyr


class MartyrSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        # Return a list of genres to create a URL for each genre filter
        return Martyr.objects.all()


class EventSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Event.objects.all()


class StaticViewSitemap(Sitemap):
    priority = 1
    changefreq = "daily"

    def items(self):
        return [
            "home",
            "martyrs",
            "news-list",
            "report-martyr",
            "report-news",
            "galleries",
            "timeline",
        ]

    def location(self, item):
        return reverse(item)


sitemaps = {
    "martyrs": MartyrSitemap,
    "statics": StaticViewSitemap,
    "events": EventSitemap,
}
