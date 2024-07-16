from django.contrib import admin

from .models import News, UserReport

# Register your models here.

admin.site.register(News)
admin.site.register(UserReport)
