from django.db import models

# Create your models here.
class Instruments(models.Model):
    instrument_name = models.CharField(max_length=20,  unique=True)
    
    def __str__(self):
        return self.instrument_name
    
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField( unique=True)
    phone_number = models.CharField(max_length=11)
    music_type = models.CharField(max_length=30, default='Classical')
    instrument_type = models.ManyToManyField(Instruments)
    
    def __str__(self):
        return self.first_name 
    
    


    
    
    