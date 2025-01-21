from django.db import models
from musician.models import Musician
from django.utils import timezone

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=50, unique=True)
    musician_name = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name="albums")
    release_date = models.DateTimeField(default=timezone.now)
    
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES, default=3)
    
    def __str__(self):
        return self.album_name
    
