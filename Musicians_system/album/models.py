from django.db import models
from musician.models import Musician

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_release_date = models.DateField()
    RATING_CHOICES = {
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    }
    rating = models.IntegerField(choices=RATING_CHOICES, default=3)
    
    def __str__(self):
        return f"{self.title} - {self.musician.user.username}"