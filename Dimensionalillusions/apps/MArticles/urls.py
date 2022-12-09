from django.conf.urls import url

# Sitemaps
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path, re_path

from .models import Article
from .views import (
    ArticleCategoryView,
    ArticleDetailView,
    ArticleSearchEngine,
    ArticleTagView,
    ArticleView,
    YourArticleDetailView,
    YourArticlesView,
    add_to_bookmark,
    bookmark_list,
    remove_from_bookmark,
)

article_dict = {
    "queryset": Article.modelmanager.filter(visibility="Public"),
}
app_name = "MArticles"

urlpatterns = [
    path(
        "articles/sitemap.xml",
        sitemap,
        {"sitemaps": {"articles": GenericSitemap(article_dict, priority=0.8, changefreq="weekly")}},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("articles/addtobookmark/<int:pk>", add_to_bookmark, name="add-to-bookmark"),
    path("articles/removefrombookmark/<int:pk>", remove_from_bookmark, name="remove-from-bookmark"),
    path("user-articles", YourArticlesView.as_view(), name="userarticles"),
    path("user-articles/<int:pk>/<slug:slug>", YourArticleDetailView.as_view(), name="yourarticle_detail"),
    path("articles", ArticleView.as_view(), name="articles"),
    path("articles/search", ArticleSearchEngine.as_view(), name="article_search"),
    path("article_detail/<int:pk>/<slug:slug>", ArticleDetailView.as_view(), name="article_detail"),
    # re_path('article_detail/(?P<slug>[-\w]+)-(?P<pk>\d+)/$',article_detail,name="article_detail"),
    path("articles/tag/<slug:slug>", ArticleTagView.as_view(), name="article-tags"),
    path("articles/category/<category>", ArticleCategoryView.as_view(), name="article-category"),
    path("articles/user-bookmarks", bookmark_list, name="user-bookmarks"),
]
