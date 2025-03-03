from django.shortcuts import render, get_object_or_404, redirect  
from . import forms
from . import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customers.models import CustomerCars, Customer
# Create your views here.

def add_brand(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        brand_form = forms.AddBrand(request.POST)
        if brand_form.is_valid():
            brand_form.save()
            messages.success(request, 'Brand Added Successfully')
            return redirect('add_brand')
    else:
        brand_form = forms.AddBrand()
    return render(request, 'brand_form.html', {'form': brand_form, 'type':'brand'})

def add_model(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        model_form = forms.AddModel(request.POST)
        if model_form.is_valid():
            model_form.save()
            messages.success(request, 'Model added successfully')
            return redirect('add_model')
    else:
        model_form = forms.AddModel()
    return render(request, 'brand_form.html', {'form': model_form, 'type':'model'})


def add_car(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        car_form = forms.AddCar(request.POST, request.FILES)  # Ensure FILES is passed

        if car_form.is_valid():
            car = car_form.save(commit=False)
            car.save() 
            messages.success(request, 'Car Added Successfully')
            return redirect('home')
            
    else:
        car_form = forms.AddCar()

    return render(request, 'car_form.html', {'form': car_form})


def car_details(request, car_id):
    car = get_object_or_404(models.Car, id=car_id)  # Get the car or return 404 if not found
    comments =  models.Comment.objects.filter(car=car).order_by('-created_at')  # Fetch comments related to the car
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to add a comment.')
            return redirect('login')
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.car = car
            comment.save()
            messages.success(request, 'Comment Added Successfully')
            return redirect('car_details', car_id=car.id)
        else:
            messages.error(request, 'There was an error submitting your comment.')
    else:
        comment_form = forms.CommentForm()
    
    context = {
        'car': car,
        'comments': comments,
        'comment_form': comment_form,
    }
    
    return render(request, 'car_details.html', context)


@login_required(login_url='login')  
def add_to_cart(request, car_id):
    if request.user.is_staff:
        messages.error(request, 'Only a Customer can add to cart')
        return redirect('home')
    
    car = get_object_or_404(models.Car, id = car_id)
    user = request.user
    customer = Customer.objects.get(customer = user)
    customer_car = CustomerCars.objects.filter(customer=customer, car=car).first()
    
    if car.quantity  > 0:
        car.quantity -= 1
        if customer_car:
            customer_car.quantity += 1
            customer_car.save()
        else:
            customer_car = CustomerCars(customer=customer, car=car, quantity=1)
            customer_car.save()
            
        car.save()
        messages.success(request, 'Car Added Successfully')
        return redirect('car_details', car_id=car.id)
    
    
def customer_profile(request):
    if request.user.is_staff:
        return redirect('home')
    
    user = request.user
    customer = Customer.objects.get(customer = user)
    customer_cars = CustomerCars.objects.filter(customer=customer).all()
    
    return render(request, 'customer_profile.html', {'cars':customer_cars})

    