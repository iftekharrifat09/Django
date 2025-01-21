from django.urls import path
from . import views

urlpatterns = [
    path('', views.customerForm, name='customerForm'),
    
    path('productform/', views.productForm, name='productform'),
    
    path('allcustomer/', views.allCustomer, name='allcustomer'),
    
    path('allproduct/', views.allProduct, name='allproduct'),
    
    path('deleteproduct/<int:id>', views.deleteaProduct, name='deleteproduct'),
    
    path('deletecustomer/<int:id>', views.deleteaCustomer, name='deletecustomer'),
]
