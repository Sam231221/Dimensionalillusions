from django.urls import path
from .views import*
from django.contrib.sitemaps import GenericSitemap # new
from django.contrib.sitemaps.views import sitemap

from MProgrammingLanguage.models import Topics

programmingtopic_dict = {
    'queryset': Topics.objects.all(),
}
app_name="ProgrammingLanguage"
urlpatterns = [
       path('pl/sitemap.xml', sitemap, # new
        {'sitemaps': {'programminglanguage': GenericSitemap(programmingtopic_dict, priority=0.8, changefreq = "weekly")}},
        name='django.contrib.sitemaps.views.sitemap'),           
      path('programminglanguages',programminglanguage,name="pl"),
      path('programminglanguage/<int:pk>/<slug:slug>',pldetail,name="pl-detail"),
      path('programminglanguage/topic/<int:pk>/<str:slug>',topicdetail,name="topic-detail"),
]
