from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            models.Customer.objects.create(customer=user)
            messages.success(request, 'Registration Successful!')
            return redirect('login')
    else:
        form = forms.RegistrationForm()
    return render(request, 'register.html', {'form': form, 'type': 'registration'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form': form, 'type': 'login'})   

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('login')         

@login_required
def update_profile(request):
    user = request.user
    print(user)
    if request.method == "POST":
        user_form = forms.EditProfileForm(request.POST, instance=user)

        if user_form.is_valid():
            user_form.save()
            return redirect('home')  # Redirect after successful update

    else:
        user_form = forms.EditProfileForm(instance=user)

    return render(request, 'update_profile.html', {
        'form': user_form,
    })