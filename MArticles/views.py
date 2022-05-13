from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, View
from EHub.forms import EmailSubscriptionForm
from MProgrammingLanguage.models import ProgrammingLanguage
from MSoftwareDevelopment.models import Framework
from taggit.models import Tag

from .forms import ArticleCommentForm, ArticleSearchForm
from .models import Article, Category, Visitior

"""
Bookmark functionality
"""


def bookmark_list(request):
    if request.user.is_authenticated:
        emailform = EmailSubscriptionForm()
        article_queryset = Article.objects.filter(bookmarks=request.user.profile, status="published")
        context = {
            "emailform": emailform,
            "article_queryset": article_queryset,
        }
        return render(request, "Articles/bookmarked-articles.html", context)
    else:
        return HttpResponse("Sign Up to Unlock this feature.")


def add_to_bookmark(request, pk):
    article_obj = get_object_or_404(Article, id=pk)
    article_obj.bookmarks.add(request.user.profile)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def remove_from_bookmark(request, pk):
    article_obj = get_object_or_404(Article, id=pk)

    article_obj.bookmarks.remove(request.user.profile)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


"""
ARTICLES 
"""


class ArticleView(View):
    def get(self, request):
        all_articles = Article.modelmanager.all().order_by(
            "published_date"
        )  # it is same as all_posts= Post.objects.filter(status="published")
        paginator = Paginator(
            all_articles, 8
        )  # creating an instance of Paginator taking all posts and create 6 items per page
        page_var = "articles"  # appears as ->/articles/?articles=2
        page = request.GET.get(page_var)  # get the string
        try:
            paginate_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginate_queryset = paginator.page(1)
        except EmptyPage:
            paginate_queryset = paginator.page(paginator.num_pages)

        context = {
            "page_var": page_var,
            "queryset": paginate_queryset,
        }
        return render(request, "Articles/article.html", context)


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "i"

    def get(self, request, pk, slug):
        emailform = EmailSubscriptionForm()
        commentform = ArticleCommentForm()
        article_obj = Article.modelmanager.get(id=pk, slug=slug)
        ip = get_client_ip(request)

        # check if visitor is added to the article
        if Visitior.objects.filter(article__id=pk).exists():
            print("The article has already this visitor")
        else:
            visitior_obj, created = Visitior.objects.get_or_create(ipaddress=ip)
            article_obj.views.add(visitior_obj)
            article_obj.total_views = article_obj.total_views + 1
            article_obj.save()

        bookmarked = bool
        if request.user.is_authenticated:
            if article_obj.bookmarks.filter(id=request.user.profile.id).exists():
                bookmarked = True

        # Comments paginate
        allcomments = article_obj.comments.filter(status=True)
        print(allcomments)
        page = request.GET.get("comments", 10)
        paginator = Paginator(allcomments, 10)  # 10 comments per page.
        try:
            comments = paginator.page(page)  # request for certain paginator   i.e page/1/
        except PageNotAnInteger:  # when page url has not an integer value, send user to page 1
            comments = paginator.page(1)
        except EmptyPage:  # when your page has just 2 but user types for page 10
            comments = paginator.page(paginator.num_pages)
        context = {
            "i": article_obj,
            "emailform": emailform,
            "comment_form": commentform,
            "comments": comments,  # recursive tree comment display
            "bookmarked": bookmarked,
            "allcomments": allcomments,  # for displaying total comments
        }

        return render(request, "Articles/articledetail.html", context)

    def post(self, request, pk, slug):
        article_obj = Article.modelmanager.get(id=pk, slug=slug)
        if request.user.is_authenticated:
            user_comment = None
            profile = request.user.profile
            if request.method == "POST":
                comment_form = ArticleCommentForm(request.POST)
                if comment_form.is_valid():
                    user_comment = comment_form.save(commit=False)
                    user_comment.article = article_obj  # set the comment post atrribute to the name of post itself
                    user_comment.user = profile
                    user_comment.save()
                    return HttpResponseRedirect(
                        reverse("MArticles:article_detail", kwargs={"pk": article_obj.id, "slug": article_obj.slug})
                    )
        else:
            return HttpResponse("login to comment")


class ArticleTagView(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        common_tags = Article.tags.most_common()[:6]
        articlesbytags = Article.modelmanager.filter(tags=tag)
        context = {
            "tag": tag,
            "common_tags": common_tags,
            "articlesbytags": articlesbytags,
        }
        return render(request, "Articles/articlesbytags.html", context)


class ArticleSearchEngine(View):
    def get(self, request):
        form = ArticleSearchForm()
        q = ""
        results = []
        query = Q()
        context = {}

        if "q" in request.GET:  # if value of key 'q' exists:
            print("User Query:", request.GET["q"])
            form = ArticleSearchForm(request.GET)
            if form.is_valid():
                q = form.cleaned_data["q"]
                results = Article.modelmanager.filter(title__search=q)
        context = {
            "q": q,
            "results": results,
        }

        return render(request, "Articles/article-search.html", context)


class ArticleCategoryView(View):
    def get(self, request, category):
        category_obj = Category.objects.get(name=category)
        article_queryset = Article.modelmanager.filter(category=category_obj)

        context = {
            "articles": article_queryset,
        }
        return render(request, "Articles/articles-by-category.html", context)


class YourArticlesView(View):
    def get(self, request):
        emailform = EmailSubscriptionForm()
        article_queryset = Article.objects.filter(visibility="Private", author=request.user.profile)
        print(article_queryset)
        context = {"emailform": emailform, "articles": article_queryset}
        return render(request, "Articles/yourarticles.html", context)


class YourArticleDetailView(View):
    def get(self, request, pk, slug):

        emailform = EmailSubscriptionForm()
        bookmarked = bool
        if request.user.is_authenticated:
            recentarticles = Article.modelmanager.order_by("-published_date")[0:4]
            article_obj = Article.objects.get(id=pk, slug=slug, visibility="Private", author=request.user.profile)
            print(article_obj)
            if article_obj.bookmarks.filter(id=request.user.profile.id).exists():
                bookmarked = True
            context = {
                "emailform": emailform,
                "recentarticles": recentarticles,
                "bookmarked": bookmarked,
                "i": article_obj,
            }
            return render(request, "Articles/yourarticle-detail.html", context)
        else:
            return HttpResponse("You do not own this article.")
