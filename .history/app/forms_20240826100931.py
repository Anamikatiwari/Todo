
from app.models import TODO
from django import forms

class TODOForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'status', 'priority']