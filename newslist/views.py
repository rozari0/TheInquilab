from django.shortcuts import render
from django.views.generic.list import ListView
from .models import News


# Create your views here.
def testrender(request):
    return render(request, template_name="base.html")


class NewsListView(ListView):
    model = News
    paginate_by = 15
    template_name = "news/newslist.html"
