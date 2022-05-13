from django.db import models
from EHub.models import *
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class ProgrammLanguage(models.Model):
    name=models.CharField(null=True,max_length=100)
    published_date = models.DateTimeField(auto_now_add = True)
  
    class Meta:
        verbose_name='Programming Language'
        verbose_name_plural='Programming Languages'        
        
    def __str__(self):
        return str(self.name)
 
def framework_image_directory_path():
    return 'Frameworks/'   

class Framework(models.Model):
    title=models.CharField(max_length=100,null=True,unique=True)
    thumbnail = models.URLField(null = True, blank = True)
    slug=models.SlugField(null=True, unique=True, editable=False) 
    description=RichTextUploadingField(null=True,config_name='default')
    language=models.ForeignKey(ProgrammLanguage,verbose_name="Programming Language",null=True,on_delete=models.SET_NULL)
    author=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    published_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return str(self.title)    
    
    def get_absolute_url(self):
        return reverse("DFramework:framework-detail", kwargs={"slug": self.slug,"pk":self.id})

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)    
        super(Framework, self).save(*args, **kwargs)     
    
class Chapter(models.Model):
    CHAPTERNUMBER_CHOICES=(
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7,7),
        (8,8),
        (9,9),
        (10,10),
        (11,11),
        (12,12),
        (13,13),
    )        
    title=models.CharField(max_length=100,null=True,unique=True)
    chapter_no = models.PositiveSmallIntegerField(verbose_name = "Chapter No" ,choices =CHAPTERNUMBER_CHOICES, null = True)
    framework=models.ForeignKey(Framework,on_delete=models.CASCADE,null=True)
 
    def __str__(self):
        return str(self.title)


class Topic(models.Model):
    DIFFICULTY_LEVEL=[
                            ('Easy','Easy'),
                            ('Medium','Medium'),
                            ('Hard','Hard'),                                                        
    ]    
    TOPICNUMBER_CHOICES=(
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7,7),
        (8,8),
        (9,9),
        (10,10),
        (11,11),
        (12,12),
        (13,13),
    )       
    
    class Meta:
        ordering=('-published_date',)
        
    def get_absolute_url(self):
        return reverse("DFramework:topic-detail", kwargs={"slug":self.slug,"pk": self.id})

    title=models.CharField(max_length=100,null=True,unique=True)
    topic_no = models.PositiveSmallIntegerField(verbose_name = "Topic No", choices = TOPICNUMBER_CHOICES ,null= True)
  
    chapter=models.ForeignKey(Chapter,on_delete=models.CASCADE,null=True)
    framework=models.ForeignKey(Framework,on_delete=models.CASCADE,null=True)    
    description = RichTextUploadingField(null=True,config_name='sourcecode',)
    slug=models.SlugField(null=True, unique=True, editable=False) 
    author=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    published_date = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now = True) 
    difficulty_level=models.CharField(choices=DIFFICULTY_LEVEL,max_length=50,null=True)
    previous_topic = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_topic = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)    

    def __str__(self):
        return str(self.title)
    
    def totalviews(self):
        return self.views.count();   
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)    
        super(Topic, self).save(*args, **kwargs)         
 

class FrameworkComment(MPTTModel):
    topic= models.ForeignKey(Topic,related_name="frameworkcomments",on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name='children')
    content = models.TextField()
    commented_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('-commented_on',)

    def __str__(self):
        return str(self.content) + ' by '+str(self.user)    
