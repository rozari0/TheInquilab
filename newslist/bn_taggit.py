from django.template.defaultfilters import slugify
from taggit.models import Tag, TaggedItem
from slugify import slugify as translate


class BnTag(Tag):
    class Meta:
        proxy = True

    def slugify(self, tag, i=None):
        return slugify(translate(self.name))[:128]


class BnTaggedItem(TaggedItem):
    class Meta:
        proxy = True

    @classmethod
    def tag_model(cls):
        return BnTag
