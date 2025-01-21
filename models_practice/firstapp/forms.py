from django import forms
from . import models

class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.CustomerModel
        fields = '__all__'
        labels = {
            'name': 'Customer Name',
            'email': 'Customer Email',
            'phone': 'Customer Phone',
            'address': 'Customer Address',
        }
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = models.ProductModel
        fields = '__all__'
        labels = {
            'title': 'Product Title',
            'price': 'Product Price',
            'description': 'Product Description',
            'image_url': 'Product Image URL',
        }