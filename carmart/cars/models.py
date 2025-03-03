from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, blank=True)
    def __str__(self):
        return self.name    
    
class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_number = models.CharField(max_length=50)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['brand', 'model_number'], name='unique_brand_model')
        ]
        
    def __str__(self):
        return self.model_number
    

class Car(models.Model):
    car_name = models.CharField(max_length=50, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car_description = models.TextField()
    
    class Meta:
        unique_together = ('brand', 'model')
    
    def __str__(self):
        return self.car_name
    
    
class Comment(models.Model):
    RATING_CHOICES = [
        (1, "⭐ (1 Star)"),
        (2, "⭐⭐ (2 Stars)"),
        (3, "⭐⭐⭐ (3 Stars)"),
        (4, "⭐⭐⭐⭐ (4 Stars)"),
        (5, "⭐⭐⭐⭐⭐ (5 Stars)"),
    ]
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="comment")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=3)
    body = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.name}"    
    
    
    