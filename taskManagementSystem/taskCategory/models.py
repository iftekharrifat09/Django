from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    CHOICE = {
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Both', 'Both')
    }
    gender_variation = models.CharField(max_length=10, choices=CHOICE, default='Both')
    
    def __str__(self):
        return self.name