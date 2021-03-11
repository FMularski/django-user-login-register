from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'user-input'})) 
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'user-input'})) 
    
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'user-input'}),
            'email': forms.EmailInput(attrs={'class': 'user-input'})
        }