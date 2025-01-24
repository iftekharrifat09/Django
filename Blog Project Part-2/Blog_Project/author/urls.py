from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/changepass/', views.change_pass, name='changepass'),
    
    path('profile/edit/', views.edit_profile, name='editprofile'),
    
]