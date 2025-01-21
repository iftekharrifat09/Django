from django.shortcuts import render, redirect
from . import forms
from django.http import HttpResponse
from . import models
# Create your views here.

def customerForm(request):
    if request.method == 'POST':
        customerform = forms.CustomerForm(request.POST)
        if customerform.is_valid():
            print(customerform.cleaned_data)
            customerform.save()
            return redirect('customerForm')
    else:
        customerform = forms.CustomerForm()
    return render(request, 'customerform.html', {'customerform': customerform})
def productForm(request):
    if request.method == 'POST':
        productform = forms.ProductForm(request.POST)
        if productform.is_valid():
            print(productform.cleaned_data)
            productform.save()
            return redirect('productform')
    else:
        productform = forms.ProductForm()
    return render(request, 'productForm.html', {'productform': productform})

def allCustomer(request):
    customers = models.CustomerModel.objects.all()
    return render(request, 'all_customer.html', {'customers': customers})

def allProduct(request):
    products = models.ProductModel.objects.all()
    return render(request, 'all_product.html', {'products': products})

def deleteaProduct(request, id):
    product = models.ProductModel.objects.get(pk=id)
    product.delete()
    return redirect('allproduct')

def deleteaCustomer(request, id):
    customer = models.CustomerModel.objects.get(pk=id)
    customer.delete()
    return redirect('allcustomer')
    