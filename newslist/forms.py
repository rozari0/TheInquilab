from django.forms import ModelForm
from .models import UserReport


class UserReportForm(ModelForm):
    class Meta:
        model = UserReport
        fields = ["title", "location", "content"]
