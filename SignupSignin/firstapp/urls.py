from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstapp, name='fistapp'),
    path('signup/', views.signUp, name='signup'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('changepassword/', views.pass_change, name='changepassword'),
    path('changepasswordWithoutOldPass/', views.pass_change_withoutOldpass, name='changepasswordWithoutOldPass'),
]
