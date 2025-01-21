from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from . import models
def task_model(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            print(task_form.cleaned_data)
            task_form.save()
            return redirect('show_task')
    else:
        task_form = forms.TaskForm()
    return render(request, 'taskmodel.html', {'task_form': task_form})

def show_task(request):
    all_task = models.TaskModel.objects.all()
    return render(request, 'show_task.html', {'all_task':all_task})

def edit_task(request, id):
    task = models.TaskModel.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    return render(request, 'taskmodel.html', {'task_form': task_form})

def delete_task(request, id):
    task = models.TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('show_task')
    
    
    
