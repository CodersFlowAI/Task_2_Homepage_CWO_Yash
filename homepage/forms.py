from django import forms
from django.core import validators
from homepage.models import Newsletter


class NewsletterForm(forms.ModelForm):
    class Meta():
        model = Newsletter
        fields = '__all__'
    