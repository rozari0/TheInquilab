from .views import testrender
from django.urls import path

urlpatterns = [
    path("base/", testrender),
]
