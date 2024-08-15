from django.contrib import admin

from .models import LongDescription, Martyr, News

# Register your models here.


class DescriptionInline(admin.StackedInline):
    model = LongDescription


@admin.action(description="Mark selected as approved")
def make_approved(modeladmin, request, queryset):
    queryset.update(approved=True)


@admin.action(description="Mark selected as not approved")
def make_not_approved(modeladmin, request, queryset):
    queryset.update(approved=False)


class MartyrAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "approved")
    list_filter = ("approved",)
    inlines = [
        DescriptionInline,
    ]
    actions = [make_approved, make_not_approved]


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "approved", "published")
    list_filter = ("approved", "is_killed")
    actions = [make_approved, make_not_approved]


admin.site.register(News, NewsAdmin)
admin.site.register(Martyr, MartyrAdmin)
