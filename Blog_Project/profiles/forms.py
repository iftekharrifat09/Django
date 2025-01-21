from django import forms
from . import models

class profileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = '__all__'