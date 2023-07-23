from django import forms
from .models import punto

class punto_form(forms.ModelForm):
    class Meta:
        model = punto
        fields = '__all__'