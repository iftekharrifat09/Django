from django import forms
from . import models

class AlbumForm(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = '__all__'
        labels = {
            'album_name': 'Album Name',
            'musician_name': 'Musician Name',
            'release_date': 'Release Data (yyyy-mm-dd hh:mm:ss)',
            'rating': 'Rating',
        }
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Enter album name'}),
        }
        
        
    