from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_model, name='task_model'),
    
    path('showtask/', views.show_task, name='show_task'),
    
    path('edit/<int:id>', views.edit_task, name='edittask'),
    
    path('delete/<int:id>', views.delete_task, name='deletetask'),
    
    
]
