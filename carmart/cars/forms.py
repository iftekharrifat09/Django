from . import models
from django import forms

class AddBrand(forms.ModelForm):
    class Meta:
        model = models.Brand
        fields = '__all__'

class AddModel(forms.ModelForm):
    class Meta:
        model = models.CarModel
        fields = '__all__'
        
class AddCar(forms.ModelForm):
    class Meta:
        model = models.Car
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'required': True, 'class': 'form-control'}),
        }
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'email', 'rating', 'body']
        

    