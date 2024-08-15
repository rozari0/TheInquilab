from django.urls import include, path

urlpatterns = [
    path("", include("newslist.api")),
]
