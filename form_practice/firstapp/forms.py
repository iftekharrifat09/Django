from django import forms
from django.core import validators
from datetime import datetime, date


class StudentForm(forms.Form):
    name =  forms.CharField(max_length=20, label='Your Full Name', widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'}))
    email = forms.EmailField(max_length=50, label='Your Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email'}))
    birth_date = forms.DateField(label="Enter Your Date of Birth",widget=forms.NumberInput(attrs={'type': 'date'}))
    
    GENDER_CHOICES = [
        ('M', 'Male'), 
        ('F', 'Female'), 
        ('O', 'Other'), 
    ]

    gender = forms.ChoiceField(
        label="Gender", 
        choices=GENDER_CHOICES, 
        widget=forms.RadioSelect()
    )
    
    COURSES = [
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
    ('Higher Mathematics', 'Higher Mathematics'),
    ]
    Select_Course = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=COURSES)
    


class feedbackForm(forms.Form):
    name = forms.CharField(label="Your Name",widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'}))
    email = forms.EmailField(label="Email Address",widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email'}))
    comment = forms.CharField(label="Write Your Opinion",widget=forms.Textarea(attrs={'placeholder': 'Enter Your Comment'}))
    agree = forms.BooleanField(label='I know what I am writing about!', required=False)
    day = forms.DateField(initial=date.today, label='Problem Facing Date (yyyy-mm-dd)')
    