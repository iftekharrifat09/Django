from django.db import models
from taskCategory.models import Category

# Create your models here.

class TaskModel(models.Model):
    task_title = models.CharField(max_length=50)
    task_description = models.TextField()
    task_completed = models.BooleanField(default=False)
    task_assign_date = models.DateTimeField()
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.task_title
