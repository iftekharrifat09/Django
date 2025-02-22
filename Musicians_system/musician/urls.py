from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_musician, name="musician_page"),
    path('register/', views.registration.as_view(), name="registration_page"),
    path('login/', views.LoginClassView.as_view(), name="login_page"),
    path('logout/', views.LogoutClassView.as_view(), name="logout"),
    path('update-data/', views.UpdateUserDataView.as_view(), name="update_user_data"),
]