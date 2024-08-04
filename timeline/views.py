from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Event


class TimelineView(ListView):
    model = Event
    context_object_name = "events"
    template_name = "timeline/timeline.html"

    def get_queryset(self):
        return Event.objects.order_by("-date", "-time")


class EventView(DetailView):
    context_object_name = "event"
    model = Event

    template_name = "timeline/event.html"
