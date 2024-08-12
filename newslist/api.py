from typing import List
from django.shortcuts import get_object_or_404
from ninja import ModelSchema, NinjaAPI
from .models import LongDescription, News, Martyr
from timeline.models import Event
from django.urls import path

api = NinjaAPI()


class EventSchema(ModelSchema):
    class Meta:
        model = Event
        fields = "__all__"


class NewsSchema(ModelSchema):
    class Meta:
        model = News
        exclude = ("approved",)


class MartyrDescriptionSchema(ModelSchema):
    class Meta:
        model = LongDescription
        exclude = ("id", "martyr_model")


class MartyrSchema(ModelSchema):
    long_description: MartyrDescriptionSchema = None

    class Meta:
        model = Martyr
        exclude = ("approved",)


@api.get("/news", response=List[NewsSchema])
def get_news_list(request):
    return News.objects.filter(approved=True)


@api.get("/news/{news_id}", response=NewsSchema)
def get_news(request, news_id: int):
    news = get_object_or_404(News, id=news_id)
    return news


@api.get("/martyr", response=List[MartyrSchema])
def get_martyr_list(request):
    return Martyr.objects.filter(approved=True)


@api.get("/martyr/{martyr_id}", response=MartyrSchema)
def get_martyr(request, martyr_id: int):
    martyr = get_object_or_404(Martyr, id=martyr_id)
    return martyr


@api.get("/timeline", response=List[EventSchema])
def get_timeline(request):
    return Event.objects.all()


@api.get("/event/{id}", response=EventSchema)
def get_event(request, id):
    event = get_object_or_404(Event, id=id)
    return event


urlpatterns = [
    path("", api.urls),
]
