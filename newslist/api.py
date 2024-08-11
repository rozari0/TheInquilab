from typing import List
from django.shortcuts import get_object_or_404
from ninja import ModelSchema, NinjaAPI
from .models import LongDescription, News, Martyr
from django.urls import path

api = NinjaAPI()


class NewsSchema(ModelSchema):
    class Meta:
        model = News
        exclude = ("approved", "tags", "tagged_items")


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


urlpatterns = [
    path("", api.urls),
]
