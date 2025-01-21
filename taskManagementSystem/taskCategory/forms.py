from django import forms
from . import models

class categoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'
        labels = {
            'name': 'Category Name',
            'gender_variation': 'Gender Variation',
        }
        widgets = {
            'gender_variation': forms.RadioSelect(),
            'name': forms.TextInput(attrs={'placeholder': 'Enter Category Name'})
        }