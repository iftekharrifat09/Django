from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

def firstapp(request):
    return render(request, 'firstapp.html')
def signUp(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.RegistrationForm(request.POST) 
            if form.is_valid():
                form.save()
                messages.success(request,'Sign Up Successful!')
                print(form.cleaned_data)
                return redirect('signup')
        else:
            form = forms.RegistrationForm()
        return render(request, 'sign_up.html', {'form': form})
    else:
        return redirect('profile')

def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            loginForm = AuthenticationForm(request.POST, data=request.POST)
            if loginForm.is_valid():
                name = loginForm.cleaned_data['username']
                userpass = loginForm.cleaned_data['password']
                user = authenticate(username=name, password=userpass) #checking is user exist into the database
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            loginForm = AuthenticationForm()
        return render(request, 'login.html', {'loginForm': loginForm})
    else:
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated:# this portion doing for edit user data
        if request.method == 'POST':
            form = forms.UserDataEdit(request.POST, instance=request.user) 
            if form.is_valid():
                form.save()
                messages.success(request,'User data updated successfully')
                return redirect('profile')
        else:
            form = forms.UserDataEdit(instance=request.user)
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('signup')

def userLogout(request):
    logout(request)
    return redirect('login')


def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pass_form = PasswordChangeForm(user=request.user, data=request.POST)
            if pass_form.is_valid():
                pass_form.save()
                update_session_auth_hash(request, pass_form.user)
                return redirect('logout')
        else:
            pass_form = PasswordChangeForm(user=request.user)
        return render(request, 'pass_change.html', {'pass_form': pass_form})
    else:
        return redirect('login')

def pass_change_withoutOldpass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pass_form = SetPasswordForm(user=request.user, data=request.POST)
            if pass_form.is_valid():
                pass_form.save()
                update_session_auth_hash(request, pass_form.user)
                return redirect('logout')
        else:
            pass_form = SetPasswordForm(user=request.user)
        return render(request, 'pass_change.html', {'pass_form': pass_form})
    else:
        return redirect('login')
    

            
            
