from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def auth(request):
    return HttpResponse('This is the authentication page.')

def user_signup(request):
    if request.method == 'POST':
        signup_form = forms.SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('login')
    else:
        signup_form = forms.SignUpForm()
    return render(request, 'signup.html', {'form': signup_form, 'type':'Sign In'})


def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is None:
                messages.error(request, 'Invalid username or password')
                return redirect('signup')
            else:
                login(request, user)
                messages.success(request, 'Logged in Successfully')
                return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('signup')
    else:
        login_form = AuthenticationForm()
    return render(request, 'signup.html', {'form':login_form, 'type':'Login'})

@login_required
def profile(request):
    user = request.user
       
    return render(request, 'profile.html', {'user':user})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out Successfully')
    return redirect('login')

@login_required
def user_edits(request):
    return render(request, 'user_edit.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit_profile_form = forms.EditProfileData(request.POST, instance = request.user)
        if edit_profile_form.is_valid():
            edit_profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        edit_profile_form = forms.EditProfileData(instance = request.user)
    return render(request, 'edit_something.html', {'form':edit_profile_form, 'type':'Profile Edit'})

@login_required
def change_password_with_old(request):
    if request.method == 'POST':
        pass_change_form = PasswordChangeForm(request.user, data=request.POST)
        if pass_change_form.is_valid():
            pass_change_form.save()
            update_session_auth_hash(request, pass_change_form.user)
            messages.success(request, 'Password Changed Successfully')
            return redirect('profile')
    else:
        pass_change_form = PasswordChangeForm(user=request.user)
    return render(request, 'edit_something.html', {'form':pass_change_form, 'type':'Password Change'})

@login_required
def change_password(request):
    if request.method == "POST":
        set_pass_form = SetPasswordForm(user=request.user, data=request.POST)
        if set_pass_form.is_valid():
            set_pass_form.save()
            update_session_auth_hash(request, set_pass_form.user)
            messages.success(request, 'Password Changed Successfully')
            return redirect('profile')
    else:
        set_pass_form = SetPasswordForm(user=request.user)
    return render(request, 'edit_something.html', {'form':set_pass_form, 'type':'Change Password Wihout Old Password'})