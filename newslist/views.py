from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic.list import ListView
from taggit.models import Tag

from .forms import MartyrReportForm, NewsReportForm
from .models import Martyr, News


# Create your views here.
def MartyrReport(request):
    form = MartyrReportForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("success")

    return render(request, template_name="martyrs/report.html", context={"form": form})


class NewsListView(ListView):
    model = News
    paginate_by = 5
    template_name = "news/newslist.html"


def NewsReport(request):
    form = NewsReportForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("success")

    return render(request, template_name="news/report.html", context={"form": form})


def tagview(request, slug):
    objects = get_object_or_404(Tag, slug=slug)
    objects = News.objects.filter(tags__slug__in=[slug])
    return render(
        request,
        template_name="news/newslist.html",
        context={"object_list": objects},
    )


class HomepageView(View):
    def get(self, request):
        news = News.objects.all()[:4]
        return render(request, template_name="home.html", context={"news_list": news})


class MartyrListView(ListView):
    model = Martyr
    paginate_by = 5
    context_object_name = "martyrs"
    template_name = "martyrs/martyrs.html"

    def get_queryset(self) -> QuerySet[Any]:
        return Martyr.objects.filter(approved=True)
