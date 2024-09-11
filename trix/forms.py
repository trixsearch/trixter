from django import forms
from .models import Trix

class TrixForm(forms.ModelForm):
    class Meta:
        model = Trix
        fields = ['text','photo']