from Dimensionalillusions.apps.EHub.forms import EmailSubscriptionForm
from Dimensionalillusions.apps.MProgrammingLanguage.models import ProgrammingLanguage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.views.generic import ListView, TemplateView, UpdateView

from .forms import FrameworkCommentForm
from .models import Chapter, Framework, FrameworkComment, Topic


def frameworks(request):
    emailform = EmailSubscriptionForm()
    renderframeworks=Framework.objects.all()
    renderpllanguages=ProgrammingLanguage.objects.all()
    context={
            'emailform':emailform,
            'pllanguages':renderpllanguages,
            'frameworks':renderframeworks,  
             }
    return render(request,'Frameworks/framework.html',context)


def frameworkdetail(request,pk,slug):
    emailform = EmailSubscriptionForm()
    renderframeworks=Framework.objects.all()
    renderpllanguages=ProgrammingLanguage.objects.all()
    print(renderpllanguages)
    getframework=Framework.objects.get(slug=slug,id=pk)
    getchapters=getframework.chapter_set.all()
    gettopics=getframework.topic_set.all()

    context={
            'emailform':emailform,
            'pllanguages':renderpllanguages,
            'frameworks':renderframeworks,  
            'i':getframework,
            'getchapters':getchapters,
            'gettopics':gettopics,
    }
    return render(request,'Frameworks/framework-detail.html',context)

def topicdetail(request,pk,slug):
    emailform = EmailSubscriptionForm()
    renderframeworks=Framework.objects.all()
    renderpllanguages=ProgrammingLanguage.objects.all()
    print(renderpllanguages)
    gettopic=Topic.objects.get(slug=slug,id=pk)
    getframework=gettopic.framework
    getchapters=getframework.chapter_set.all()
    comment_form = FrameworkCommentForm

    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip           
    
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
            print("Ip Already exist")
            gettopic.views.add(IpModel.objects.get(ip=ip))
    
    else:   
            IpModel.objects.create(ip=ip)
            gettopic.views.add(IpModel.objects.get(ip=ip))
  
    allcomments = gettopic.frameworkcomments.filter(status=True)     
    page = request.GET.get('comments', 10)#doesn't matter whatever String you mention on the parameter. i.e you mention string replacing comments it works still.
    
    paginator = Paginator(allcomments, 10)#10 comments per page.
    try:
        comments = paginator.page(page)#request for certain paginator   i.e page/1/
    except PageNotAnInteger:#when page url has not an integer value, send user to page 1
        comments = paginator.page(1)
    except EmptyPage: #when your page has just 2 but user types for page 10
        comments = paginator.page(paginator.num_pages)
        
    user_comment = None
    profile=request.user.profile   
    if request.method == 'POST':
        comment_form = FrameworkCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            print(user_comment)
            print(gettopic.id)
            user_comment.topic = gettopic#set the comment post atrribute to the name of post itself
            print(user_comment.topic)
            user_comment.user = profile
            user_comment.save()
            return HttpResponseRedirect(reverse('DFramework:topic-detail',kwargs={"slug":gettopic.slug,'pk':gettopic.id}))
    
    context={
            'pllanguages':renderpllanguages,
            'frameworks':renderframeworks,  
        
            'emailform':emailform,
            'getchapters':getchapters,
            "i":gettopic,
            'comments': comments,
            'allcomments': allcomments,
            'comment_form': comment_form        
    }
    return render(request,'Frameworks/topic-detail.html',context)
