from django.contrib.sitemaps import Sitemap

from .models import Article


class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Article.modelmanager.all()

    def lastmodified(self, obj):
        return obj.last_updated
