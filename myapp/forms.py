from django import forms
from myapp.models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TaskForm(forms.ModelForm):
    
    # created_date=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"date","class":"form-control"}))
    
    class Meta:
        
        model=Task
        fields= ["title","discription","task_status","Due_date"]
        
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "discription":forms.TextInput(attrs={"class":"form-control"}),
            "task_status":forms.CheckboxInput(attrs={"class":"form-check-input"}),
            "Due_date": forms.DateTimeInput(attrs={"class":"form-control",
                                                   "type":"datetime-local"})
            
        }
        
class RegisterForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-2"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-2"}))
    
    class Meta:
        
        model= User
        
        fields = ["username","email","password1","password2"]
        
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control mb-2"}),
            "email":forms.EmailInput(attrs={"class":"form-control mb-2"})
             
        }
        
class LoginForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control,mb-3"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control,mb-3"}))
    
    
        