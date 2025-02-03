from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Employee, AllowedEmail, DefaultHoliday, EmployeeHoliday, MessageBox, Task

class EmployeeRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not AllowedEmail.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is not allowed. Please contact admin.")
        return email

class EmployeeUpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = Employee
        fields = ['sector', 'position']

class AllowedEmailForm(forms.ModelForm):
    class Meta:
        model = AllowedEmail
        fields = ['email']

class AdminSetPasswordForm(forms.ModelForm):
    new_password = forms.CharField(widget=forms.PasswordInput, label="New Password")

    class Meta:
        model = User
        fields = []

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data['new_password'])
        if commit:
            user.save()
        return user

class UserUpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
class DefaultHolidayForm(forms.ModelForm):
    class Meta:
        model = DefaultHoliday
        fields = ['day']

class MultiDateHolidayForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), label="Select Employee")
    holiday_dates = forms.CharField(widget=forms.TextInput(attrs={'class': 'multi-date-picker', 'placeholder': 'Select multiple dates'}), label="Holiday Dates")
    
class MultiDefaultHolidaysForm(forms.Form):
    holiday_dates = forms.CharField(widget=forms.TextInput(attrs={'class': 'multi-date-picker', 'placeholder': 'Select multiple dates'}), label="Holiday Dates")
        

class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageBox
        fields = ['name', 'email', 'message']
        

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("Start date cannot be after end date.")
        
        return cleaned_data