from django.urls import path
from django.shortcuts import render
from .views import NewsListView, report, tagview, ReportListView, ReportDetailView

urlpatterns = [
    path("news/", NewsListView.as_view(), name="news-list"),
    path("tag/<slug:slug>", tagview, name="tagbase-view"),
    path("report/", report, name="report-view"),
    path(
        "success/",
        lambda request: render(request, template_name="news/successreport.html"),
        name="success",
    ),
    path("", lambda request: render(request, template_name="home.html"), name="home"),
    path("reports/", ReportListView.as_view(), name="report-list"),
    path("reports/<int:pk>/", ReportDetailView.as_view(), name="report-detail"),
]
