from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Adjust fields as needed

    # Optional: Customize field widgets if needed
    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
    }