from .forms import ArticleSearchForm
from .models import Article, Category


def articlefilters(request):
    return {
        "form": ArticleSearchForm(),
        "categories": Category.objects.all(),
        "populararticles": Article.modelmanager.order_by("-total_views")[0:4],
        "recentarticles": Article.modelmanager.order_by("-published_date")[0:4],
    }
