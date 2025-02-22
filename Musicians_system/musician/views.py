from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import UpdateView
from django.contrib import messages
from . import models
from . import forms
from django.urls import reverse_lazy
# Create your views here.
def musician(request):
    return render(request, 'musician_page.html')


class registration(CreateView):
    model = models.Musician  
    form_class = forms.RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('registration_page')  
    def form_valid(self, form):
        
        if form.is_valid():
            return super().form_valid(form)
        else:
            return self.form_invalid(form)  
        
        
class LoginClassView(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('home_page')
    
    def form_valid(self, form):
        messages.success(self.request, 'You are logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return super().form_invalid(form)
    
    
class LogoutClassView(LogoutView):
    next_page = reverse_lazy('login_page')  # Redirect after logout
    
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out successfully.")  # Add message
        return super().dispatch(request, *args, **kwargs)
    
    
    
class UpdateUserDataView(UpdateView): 
    model = models.Musician
    form_class = forms.UpdateMusicianForm
    template_name = 'update_data.html'  # Update this if necessary
    success_url = reverse_lazy('home_page')

    def get_object(self):
        """Ensure the logged-in musician's profile is being edited."""
        return self.request.user.musician  
    
    
def all_musician(request):
    musicians = models.Musician.objects.all()
    return render(request, 'musician_page.html', {'musicians': musicians})
        
    
    

    