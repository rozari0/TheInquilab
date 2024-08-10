from django.urls import path

from . import views

urlpatterns = [
    path("timeline/", views.TimelineView.as_view(), name="timeline"),
    path("event/<slug:slug>/", views.EventView.as_view(), name="event"),
]
