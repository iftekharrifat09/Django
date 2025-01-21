from django import forms
from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.TaskModel
        fields = '__all__'
        labels = {
            'task_title': 'Task Title',
            'task_description': 'Task Description',
            'task_completed': 'Task Completed?',
            'task_assign_date': 'Task Assign Date',
            'category': 'Task Category',
        }
        
        widgets = {
            'task_assign_date': forms.DateInput(attrs={'type': 'date'}),
            'task_title': forms.TextInput(attrs={'placeholder':'Enter task title'}),
            'task_description': forms.Textarea(attrs={'placeholder': 'Enter Task Description'})
        }