from django.db import models
from django.contrib.auth.models import User
from cars.models import Car
# Create your models here.


class Customer(models.Model):
    customer = models.OneToOneField(User, related_name="customers", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.customer.username
    
    
class CustomerCars(models.Model):
    customer = models.ForeignKey(Customer, related_name="cars", on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name="cars", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.customer.customer.username}'s car {self.car.model}"