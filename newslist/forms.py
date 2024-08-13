from django.forms import DateField, DateInput, ModelForm

from .models import Martyr, News


class MartyrReportForm(ModelForm):
    birth = DateField(widget=DateInput(attrs={"type": "date"}), required=False)
    death = DateField(widget=DateInput(attrs={"type": "date"}), required=False)

    class Meta:
        model = Martyr
        exclude = ("approved",)


class NewsReportForm(ModelForm):
    published = DateField(widget=DateInput(attrs={"type": "date"}), required=False)

    class Meta:
        model = News
        exclude = ("approved",)
