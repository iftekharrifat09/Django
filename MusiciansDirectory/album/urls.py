from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_album, name='add_album'),
]
