from django.db import models
from categories.models import Category
from author.models import Author

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    category = models.ManyToManyField(Category) # eta post er moddhe multiple category thakte pare, abar ekta category multiple post er moddhe thakte pare.
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #models.CASCADE er mane holo, jodi amra kono Author ke delete kore dei tahole tar sob details delete hoye jabe.
    
    def __str__(self):
        return self.title