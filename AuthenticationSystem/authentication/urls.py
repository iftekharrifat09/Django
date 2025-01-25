from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('user_edits/', views.user_edits, name='useredit'),
    path('profile_edit/', views.edit_profile, name='editprofile'),
    path('change_pass_old/', views.change_password_with_old, name='changepassword1'),
    path('change_pass/', views.change_password, name='changepassword2'),
]
