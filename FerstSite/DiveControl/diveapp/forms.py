from django import forms
from .models import Diver



class DiverProfileForm(forms.ModelForm):
    class Meta:
        model = Diver
        fields = ['ime', 'prezime', 'oib']