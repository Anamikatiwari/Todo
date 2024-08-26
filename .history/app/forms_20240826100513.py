from django.forms import from django import forms
from app.models import TODO

class TODOForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'status']
from app.models import TODO
from django import forms

class TODOForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'status', 'priority']