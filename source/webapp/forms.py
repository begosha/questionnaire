from django import forms
from .models import Poll, Choice

class SimpleSearchForm(forms.Form):

    search = forms.CharField(max_length=100, required=False, label="Search")