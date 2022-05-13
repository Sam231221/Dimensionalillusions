from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *


class SuperArticleModel(admin.ModelAdmin):
    exclude = (
        "contenttype",
        "bookmarks",
    )
    list_display = (
        "title",
        "visibility",
        "id",
        "published_date",
        "last_updated",
        "author",
    )
    list_filter = ["status", "author", "category", "visibility"]
    search_fields = ["title", "description"]


admin.site.register(Article, SuperArticleModel)  # an way of extending model showing fields in admin section

admin.site.register(AComment, MPTTModelAdmin)

admin.site.register((Category, Visitior))
