from django.contrib import admin

from .models import LongDescription, Martyr, News

# Register your models here.


class DescriptionInline(admin.StackedInline):
    model = LongDescription


class MartyrAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "approved")
    list_filter = ("approved",)
    inlines = [
        DescriptionInline,
    ]


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "approved")
    list_filter = ("approved", "is_killed")


admin.site.register(News, NewsAdmin)
admin.site.register(Martyr, MartyrAdmin)
