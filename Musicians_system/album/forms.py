from django import forms
from . import models
from datetime import date

class AlbumForm(forms.ModelForm):
    album_release_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), initial=date.today
    )
    class Meta:
        model = models.Album
        exclude = ['musician']