from django.db import models
from django.utils import timezone

class CustomerModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    
    def __str__(self):
        return self.name
    
class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
    