from ckeditor_uploader.fields import RichTextUploadingField
from Dimensionalillusions.apps.EHub.models import Profile
from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey

app_name="ProgrammingLanguage"


def programminglanguage_image_directory_path():
    return 'ProgrammingLanguages/'

class ProgrammingLanguage(models.Model):
    title=models.CharField(max_length=100,null=True,unique=True)
    thumbnail = models.URLField(null = True, blank = True)
    
    slug=models.SlugField(null=True, unique=True, editable=False) 
    description=RichTextUploadingField(null=True,config_name='default')
    author=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    published_date = models.DateTimeField(auto_now_add = True)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)    
        super(ProgrammingLanguage, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.title)    
    
    def get_absolute_url(self):
        return reverse("ProgrammingLanguage:pl-detail", kwargs={"slug": self.slug,"pk":self.id})
    
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
    chapter_no = models.PositiveSmallIntegerField(verbose_name = "Chapter No" , choices =CHAPTERNUMBER_CHOICES, null = True)
    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE, null=True)
    class Meta:
        ordering = ('chapter_no',)    
    
    def __str__(self):
        return str(self.title)


class Topics(models.Model):
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
        ordering = ('topic_no',)
        
    def get_absolute_url(self):
        return reverse("ProgrammingLanguage:topic-detail", kwargs={"slug":self.slug,"pk": self.id})

    title = models.CharField(max_length=100,null=True,unique=True)
    topic_no = models.PositiveSmallIntegerField(verbose_name = "Topic No", choices = TOPICNUMBER_CHOICES ,null= True)
    chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE,null=True)
    planguage = models.ForeignKey(ProgrammingLanguage,on_delete=models.CASCADE,null=True)    
    description = RichTextUploadingField(null=True,config_name='sourcecode',)
    slug = models.SlugField(null=True, unique=True, editable=False) 
    author = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    
    published_date = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now = True) 
    
    difficulty_level = models.CharField(choices=DIFFICULTY_LEVEL,max_length=50,null=True)
    previous_topic = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_topic = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)    

    def __str__(self):
        return str(self.title)
    
    def totalviews(self):
        return self.views.count();   
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)    
        super(Topics, self).save(*args, **kwargs)    
    
class PLComment(MPTTModel):
    topics = models.ForeignKey(Topics,related_name="plcomments",on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name='children')
    content = models.TextField()
    commented_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('-commented_on',)

    def __str__(self):
        return str(self.content) + ' by '+str(self.user)    
