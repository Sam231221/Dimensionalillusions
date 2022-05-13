from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *

# Register your models here.
admin.site.register((ProgrammLanguage,Chapter))
admin.site.register(FrameworkComment,MPTTModelAdmin)

class FrameworkModel(admin.ModelAdmin):
    list_display=('title','language','thumbnail','author')
admin.site.register(Framework, FrameworkModel)

class TopicModel(admin.ModelAdmin):
    list_display=('title','framework','chapter','author')
admin.site.register(Topic, TopicModel)