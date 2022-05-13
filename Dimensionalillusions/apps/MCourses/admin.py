from django.contrib import admin
from .models import Chapter, Topic, Course, CSComment

class TopicAdmin(admin.ModelAdmin):
    exclude =('views',)
    list_display=['title', 'topic_no', 'author' ,'chapter']
    list_filter = ['chapter',]           
admin.site.register(Topic, TopicAdmin)       
class ChapterAdmin(admin.ModelAdmin):
    list_display=['title', 'chapter_no', 'course']
    list_filter = ['course',]           
             
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Course)
admin.site.register(CSComment)
