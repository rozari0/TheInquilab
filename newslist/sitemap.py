from django.contrib.sitemaps import Sitemap

from .models import Martyr


class MartyrSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        # Return a list of genres to create a URL for each genre filter
        return Martyr.objects.all()


sitemaps = {
    "martyrs": MartyrSitemap,
}
