from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from . import models


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    first_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'})
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'})
    )
    

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
        }
        
class EditProfileForm(UserChangeForm):
    password = None  # Hide password field

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        