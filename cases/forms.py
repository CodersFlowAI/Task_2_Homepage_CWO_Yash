from django import forms
from django.core import validators
from cases.models import ReportAnonymously
from cases.models import Report


class ReportAnonymouslyForm(forms.ModelForm):
    class Meta():
        model = ReportAnonymously
        exclude=['date_subscribed']
        


class ReportForm(forms.ModelForm):
    class Meta():
        model = Report
        exclude=['date_subscribed']
        