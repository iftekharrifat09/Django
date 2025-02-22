from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = PhoneNumberField(region="BD", widget=forms.TextInput(attrs={'class': 'phone-input'}))  # Add class for JS styling
    instrument_type = forms.CharField(max_length=50)
    

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number', 'instrument_type']


    def save(self, commit=True):
        user = super().save(commit=False)  # ✅ Use `super()`
        if commit:
            user.save()
            models.Musician.objects.create(   # ✅ Corrected the model reference
                user=user,
                instrument_type=self.cleaned_data['instrument_type'],
                phone_number=self.cleaned_data['phone_number']
            )
        return user
    
    
class UpdateMusicianForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = models.Musician
        fields = ['phone_number', 'instrument_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate user fields
        if self.instance and self.instance.user:
            self.fields['username'].initial = self.instance.user.username
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        musician = super().save(commit=False)
        user = musician.user  # Get the linked User instance

        # Update User fields
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()  # Save User model first
            musician.save()  # Then save Musician model

        return musician