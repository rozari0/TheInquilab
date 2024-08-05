from django.contrib import admin

from .models import Martyr, News, UserReport, LongDescription

# Register your models here.


class DescriptionInline(admin.StackedInline):
    model = LongDescription


class MartyrAdmin(admin.ModelAdmin):
    inlines = [
        DescriptionInline,
    ]


admin.site.register(News)
admin.site.register(UserReport)
admin.site.register(Martyr, MartyrAdmin)
