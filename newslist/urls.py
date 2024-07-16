from .views import NewsListView
from django.urls import path

urlpatterns = [
    path("base/", NewsListView.as_view(), name="news-list"),
]
