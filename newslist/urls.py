from .views import NewsListView, tagview
from django.urls import path

urlpatterns = [
    path("news/", NewsListView.as_view(), name="news-list"),
    path("tag/<slug:slug>", tagview, name="tagbase-view"),
]
