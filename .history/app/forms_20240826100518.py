from django import forms
from app.models import TODO

class TODOForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'status']