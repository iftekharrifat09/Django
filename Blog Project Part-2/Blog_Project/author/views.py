from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post

# Create your views here.

# def add_author(request):
    
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form = forms.AuthorForm()
        
#     return render(request, 'add_author.html', {'author_form': author_form})

def register(request):
    if request.method == 'POST':
        reg_form = forms.RegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('login')
    else:
        reg_form = forms.RegistrationForm()
    return render(request,'registration.html', {'form': reg_form, 'type':'Registration'})

def userLogin(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST) 
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is None:
                messages.error(request, "Invalid username or password")
                return redirect('login')
            else:
                login(request, user)
                messages.success(request, "Logged in successfully")
                return redirect('profile')
        else:
            messages.warning(request, 'Invalid form data')  
            return redirect('register') 
    else:
        login_form = AuthenticationForm()

    return render(request, 'registration.html', {'form': login_form, 'type': 'Login'})

@login_required
def profile(request):
    data = Post.objects.filter(author=request.user)
    return render(request,'profile.html', {'data': data}) 

@login_required
def change_pass(request):
    if request.method == 'POST':
        passChangeForm = PasswordChangeForm(request.user, data=request.POST)
        if passChangeForm.is_valid():
              passChangeForm.save()
              update_session_auth_hash(request, passChangeForm.user)
              messages.success(request, 'Password Changed Successfully')
              return redirect('profile')
    else:
        passChangeForm = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html',{'form': passChangeForm})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserData(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserData(instance=request.user)
    return render(request,'edit_profile.html', {'form': profile_form}) 

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')