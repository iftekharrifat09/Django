from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Musician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True, verbose_name="Phone number", region="BD")  # Default region Bangladesh
    instrument_type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username