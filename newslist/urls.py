from django.shortcuts import render
from django.urls import path

from .views import (
    HomepageView,
    MartyrListView,
    NewsListView,
    report,
    tagview,
)

urlpatterns = [
    path("news/", NewsListView.as_view(), name="news-list"),
    path("tag/<slug:slug>", tagview, name="tagbase-view"),
    path("report/", report, name="report-view"),
    path(
        "success/",
        lambda request: render(request, template_name="news/successreport.html"),
        name="success",
    ),
    path("", HomepageView.as_view(), name="home"),
    path("martyrs/", MartyrListView.as_view(), name="martyrs"),
]
