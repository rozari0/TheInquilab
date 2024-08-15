from django.shortcuts import render
from django.urls import path

from .views import (
    HomepageView,
    MartyrDetailView,
    MartyrListView,
    MartyrReport,
    NewsListView,
    NewsReport,
)

urlpatterns = [
    path("news/", NewsListView.as_view(), name="news-list"),
    path("report/martyr/", MartyrReport, name="report-martyr"),
    path("report/news/", NewsReport, name="report-news"),
    path(
        "success/",
        lambda request: render(request, template_name="news/successreport.html"),
        name="success",
    ),
    path("", HomepageView.as_view(), name="home"),
    path("martyrs/", MartyrListView.as_view(), name="martyrs"),
    path("martyr/<slug:slug>/", MartyrDetailView.as_view(), name="martyr"),
]
