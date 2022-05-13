from .models import *
from MSoftwareDevelopment.models import Framework
from django.shortcuts import render

from EHub.forms import EmailSubscriptionForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from .forms import *


# Create your views here.
def programminglanguage(request):
    emailform = EmailSubscriptionForm()
    renderframeworks=Framework.objects.all()
    context={
                 'emailform':emailform,
                 'frameworks':renderframeworks,
             }
    return render(request,'ProgrammingLanguages/pl.html',context)

def pldetail(request,pk,slug):
    emailform = EmailSubscriptionForm()
    getpl=ProgrammingLanguage.objects.get(slug=slug,id=pk)
    renderpllanguages=ProgrammingLanguage.objects.all()
    renderframeworks=Framework.objects.all()    
    getchapters=getpl.chapter_set.all()
    gettopics=getpl.topics_set.all()

    context={
            'emailform':emailform,
            'i':getpl,
            'getchapters':getchapters,
            'gettopics':gettopics,
            'pllanguages':renderpllanguages,
            'frameworks':renderframeworks,    
    }
    
    return render(request,'ProgrammingLanguages/pl_detail.html',context)

def topicdetail(request,pk,slug):
    emailform = EmailSubscriptionForm()
    gettopic=Topics.objects.get(slug=slug,id=pk)
    getpl=gettopic.planguage
    getchapters=getpl.chapter_set.all()
    comment_form = PlcommentForm()
    renderpllanguages=ProgrammingLanguage.objects.all()
    renderframeworks=Framework.objects.all()

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
    allcomments = gettopic.plcomments.filter(status=True)     
    page = request.GET.get('comments', 10)
    
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
            comment_form = PlcommentForm(request.POST)
            if comment_form.is_valid():
                user_comment = comment_form.save(commit=False)
                print(user_comment)
                print(gettopic.id)
                user_comment.topics = gettopic
                print(user_comment.topics)
                user_comment.user = profile
                user_comment.save()
                return HttpResponseRedirect(reverse('ProgrammingLanguage:topic-detail',kwargs={"slug":gettopic.slug,'pk':gettopic.id}))
        
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
            #'comment_form': comment_form,   
            
            'pllanguages':renderpllanguages,
            'frameworks':renderframeworks,    
        }            
    return render(request,'ProgrammingLanguages/topicdetail.html',context)