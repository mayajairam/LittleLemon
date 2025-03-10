from django import forms
from django.forms.widgets import NumberInput
from .models import Logger


class DemoForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'