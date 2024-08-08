from django.contrib import admin

from .models import Martyr, News, LongDescription

# Register your models here.


class DescriptionInline(admin.StackedInline):
    model = LongDescription


class MartyrAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "approved")
    list_filter = ("approved",)
    inlines = [
        DescriptionInline,
    ]


admin.site.register(News)
admin.site.register(Martyr, MartyrAdmin)
