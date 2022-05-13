from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Chapter)

class PLAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail', 'slug', 'author')
admin.site.register(ProgrammingLanguage, PLAdmin)

class TopicsAdmin(admin.ModelAdmin):
    list_display = ('title','chapter','planguage', 'slug', 'author')

admin.site.register(Topics,TopicsAdmin)

from mptt.admin import MPTTModelAdmin
admin.site.register(PLComment, MPTTModelAdmin)
