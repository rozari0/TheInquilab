from django.forms import ModelForm, DateField, DateInput

from .models import Martyr


class MartyrReportForm(ModelForm):
    birth = DateField(widget=DateInput(attrs={"type": "date"}), required=False)
    death = DateField(widget=DateInput(attrs={"type": "date"}), required=False)

    class Meta:
        model = Martyr
        exclude = ("approved",)
