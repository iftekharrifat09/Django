from django import forms
from . import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = '__all__'
        
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_number': 'Phone Number',
            'music_type': 'Music Type',
            'instrument_type': 'Instrument Type',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
        
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter Phone Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Your Email'})
        }
    
        
class InstrumentForm(forms.ModelForm):
    class Meta:
        model = models.Instruments
        fields = '__all__'
        
        labels = {
            'instrument_name': 'Instrument Name',
        }
        widgets = {
            'instrument_name': forms.TextInput(attrs={'placeholder': 'Enter Instrument Name'}),
        }