from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from . import models
# Create your views here.

studentData = []
def studentInfo(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            studentData.clear()
            studentData.append(form.cleaned_data)
            print(form.cleaned_data)
            return redirect('seeStudentInfo')
    else:
        form = forms.StudentForm()
    return render(request, 'student_form.html', {'form': form})

def seeStudentInfo(request):
    return render(request, 'seeStudentInfo.html', {'studentData': studentData[0]})

feedbackData = [] 
def feedback(request):
    if request.method == "POST":
        form = forms.feedbackForm(request.POST)
        if form.is_valid():
            feedbackData.clear()
            feedbackData.append(form.cleaned_data)
            print(form.cleaned_data)
            return redirect('seeFeedback')
    else:
        form = forms.feedbackForm()   
    return render(request, 'feedback_form.html', {'form': form})


def seefeedback(request):
    return render(request, 'seeFeedback.html', {'feedbackData': feedbackData[0]})

def about(request):
    return render(request, 'aboutUs.html')