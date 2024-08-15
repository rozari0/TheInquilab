from typing import Any

from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView, ListView

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

    def get_queryset(self) -> QuerySet[Any]:
        return self.model.objects.filter(approved=True)


def NewsReport(request):
    form = NewsReportForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("success")

    return render(request, template_name="news/report.html", context={"form": form})


class HomepageView(View):
    def get(self, request):
        news = News.objects.all()[:4]
        return render(request, template_name="home.html", context={"news_list": news})


class MartyrListView(ListView):
    model = Martyr
    paginate_by = 30
    context_object_name = "martyrs"
    template_name = "martyrs/martyrs.html"

    def get_queryset(self) -> QuerySet[Any]:
        return self.model.objects.filter(approved=True)


class MartyrDetailView(DetailView):
    context_object_name = "martyr"
    model = Martyr

    template_name = "martyrs/martyrs_details.html"
