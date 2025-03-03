from django.urls import path
from . import views

urlpatterns = [
    path('add-brand/', views.add_brand, name='add_brand'), 
    path('add-model/', views.add_model, name='add-model'), 
    path('add-car/', views.add_car, name='add-car'),  
    path('car-details/<int:car_id>', views.car_details, name='car_details'),  
    path('add-to-cart/<int:car_id>', views.add_to_cart, name='add_to_cart'),   
    path('profile/', views.customer_profile, name='profile'),   
]
