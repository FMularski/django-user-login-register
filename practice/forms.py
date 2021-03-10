from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'user-input'}),
            'email': forms.EmailInput(attrs={'class': 'user-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'user-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'user-input'})
        }