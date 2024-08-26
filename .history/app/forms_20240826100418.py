from django.forms import ModelForm
from app.models import TODO
from django import forms

class TODOForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'status', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.RadioSelect()
        }