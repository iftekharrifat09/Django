from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_musician, name='add_musician'),
    path('instrument/', views.add_instrument, name='add_instrument'),
    
    path('alldata/', views.showingData, name='alldata'),
    
    path('editmusician/<int:id>', views.edit_musician, name='editmusician'),
    
    path('deletemusician/<int:id>', views.delete_musician, name='deletemusician'),
    
    
]
