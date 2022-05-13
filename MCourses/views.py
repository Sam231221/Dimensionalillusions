from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.views.generic import View
from EHub.forms import EmailSubscriptionForm
from MProgrammingLanguage.models import ProgrammingLanguage
from MSoftwareDevelopment.models import Framework

from MCourses.models import Course

from .forms import *
from .models import *


class CoursesView(View):
    def get(self, request):
        emailform = EmailSubscriptionForm()
        renderpllanguages=ProgrammingLanguage.objects.all()
        renderframeworks=Framework.objects.all()    
        
        all_courses =Course.modelmanager.all()
        paginator=Paginator(all_courses, 12)
        page_var='articles' 
        page=request.GET.get(page_var)
        try:
            paginate_queryset=paginator.page(page)
        except PageNotAnInteger:
            paginate_queryset=paginator.page(1)
        except EmptyPage:
            paginate_queryset=paginator.page(paginator.num_pages)      
        
        context={
                    'page_var':page_var,
                    'queryset' : paginate_queryset,    
                    'emailform':emailform,
                    'pllanguages':renderpllanguages,
                    'frameworks':renderframeworks,
        }
        return render(request,'Courses/courses.html',context)

def coursedetail(request,pk,slug):
    emailform = EmailSubscriptionForm()    
    rendercourse=Course.objects.get(id=pk,slug=slug)
    getchapters=rendercourse.chapter_set.all()
    renderpllanguages=ProgrammingLanguage.objects.all()
    renderframeworks=Framework.objects.all()
    
    context={
           'emailform':emailform,
            'course':rendercourse,
            'getchapters':getchapters,
            'pllanguages':renderpllanguages,
            'frameworks':renderframeworks,
        
    }
    return render(request,'Courses/course-detail.html',context)

def topicdetail(request,pk,slug):
    emailform = EmailSubscriptionForm()    
    comment_form = CourseCommentForm()
    
    gettopic=Topic.objects.get(id=pk,slug=slug)
    getcourse=gettopic.chapter.course
    getchapters=getcourse.chapter_set.all()
    
    renderpllanguages=ProgrammingLanguage.objects.all()
    renderframeworks=Framework.objects.all()
    

       
    allcomments = gettopic.coursecomments.filter(status=True)     
    page = request.GET.get('comments', 10)#
    paginator = Paginator(allcomments, 10)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage: 
        comments = paginator.page(paginator.num_pages)

    context={}
    if request.user.is_authenticated:           
        user_comment = None
        profile=request.user.profile   
        if request.method == 'POST':
            comment_form = CourseCommentForm(request.POST)
            if comment_form.is_valid():
                user_comment = comment_form.save(commit=False)
                print(gettopic.id)
                user_comment.topic = gettopic
                print(user_comment.topic)
                user_comment.user = profile
                user_comment.save()
                print(user_comment)
                return HttpResponseRedirect(reverse('Courses:topic-detail',kwargs={"slug":gettopic.slug,'pk':gettopic.id}))
        
        context={
            'emailform':emailform,
            'getchapters':getchapters,
            "i":gettopic,
            'comments': comments,
            'allcomments': allcomments,
            'comment_form': comment_form,
            
            'pllanguages':renderpllanguages,
            'frameworks':renderframeworks,          
        }
    else:
        context={
            'emailform':emailform,
            'getchapters':getchapters,
            "i":gettopic,
            'comments': comments,
            'allcomments': allcomments,
            
            'pllanguages':renderpllanguages,
            'frameworks':renderframeworks,          
        }            
    return render(request,'Courses/topic-detail.html',context)
