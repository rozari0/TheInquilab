from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from taggit.models import Tag

from .forms import UserReportForm
from .models import News, UserReport


# Create your views here.
def report(request):
    form = UserReportForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("success")

    return render(request, template_name="news/report.html", context={"form": form})


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


class ReportListView(ListView):
    model = UserReport
    paginate_by = 15
    template_name = "news/reportlist.html"

    def get_queryset(self):
        return UserReport.objects.filter(approved=False)


class ReportDetailView(DetailView):
    model = UserReport
    template_name = "news/reportdetail.html"
