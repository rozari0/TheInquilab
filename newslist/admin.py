from django.contrib import admin

from .models import Martyr, News, UserReport

# Register your models here.

admin.site.register(News)
admin.site.register(UserReport)
admin.site.register(Martyr)
