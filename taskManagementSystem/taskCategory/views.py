from django.shortcuts import render, redirect
from . import forms
# Create your views here.

def task_category(request):
    if request.method == 'POST':
        category_form = forms.categoryForm(request.POST)
        if category_form.is_valid():
            print(category_form.cleaned_data)
            category_form.save()
            return redirect('task_model')
    else:
        category_form = forms.categoryForm()
    return render(request, 'category.html', {'category_form': category_form})