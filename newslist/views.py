from django.shortcuts import render
from django.views.generic.list import ListView
from .models import News
from taggit.models import Tag
from django.shortcuts import get_object_or_404


# Create your views here.
def testrender(request):
    return render(request, template_name="base.html")


class NewsListView(ListView):
    model = News
    paginate_by = 15
    template_name = "news/newslist.html"


def tagview(request, slug):
    objects = get_object_or_404(Tag, slug=slug)
    objects = News.objects.filter(tags__slug__in=[slug])
    return render(
        request,
        template_name="news/newslist.html",
        context={"object_list": objects},
    )
