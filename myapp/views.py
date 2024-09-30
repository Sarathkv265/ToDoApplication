from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.forms import TaskForm,RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from myapp.models import Task
from myapp.decorators import auth_required
from django.utils.decorators import method_decorator



class SignupView(View):
    def get(self,request,*args,**kwargs):
        
        form_instance=RegisterForm()
        
        return render(request,"signup.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_instance = RegisterForm(request.POST)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            messages.success(request,"siginup successful..!")
            
            return redirect("signin")
            
        else :
            
            messages.error(request,"signup unsccessful..!")
            
            return render(request,"signup.html",{"form":form_instance})
        
class SigninView(View):
    def get(self,request,*args,**kwargs):
        
        form_instance = LoginForm()
        
        return render(request,"signin.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_instance = LoginForm(request.POST)
        
        if form_instance.is_valid():
            
            user_object=authenticate(request,**form_instance.cleaned_data)
            
            if user_object:
                
                login(request,user_object)
                
                messages.success(request,"Login successful...!")
                return redirect("todo-list")
        messages.error(request,"Login Unsuccessful...!")
        return render(request,"signin.html",{"form":form_instance})

@method_decorator(auth_required, name="dispatch")   
class SignoutView(View):
    
    def get(self,request,*args,**kwargs):
        
        logout(request)
        
        return redirect("signin")
    
        
class ToDoCreateView(View):
    
    def get(self,request,*args,**kwargs):
        
        form_instance = TaskForm()
        
        return render(request,"todocreate.html",{"form":form_instance})
    def post(self,request,*args,**kwargs):
        
        form_instance = TaskForm(request.POST)
        
        if form_instance.is_valid():
        
            form_instance.instance.owner=request.user
            
            form_instance.save()
            
            return redirect("todo-list")
        return render(request,"todocreate.html",{"form":form_instance})
@method_decorator(auth_required,name="dispatch")   
class ToDoListView(View):
    
    def get(self,request,*args,**kwargs):
        
        qs=Task.objects.filter(owner=request.user)
        
        return render(request,"todo_list.html",{"lists":qs})
    
    
@method_decorator(auth_required, name="dispatch")   
class ToDoUpdateView(View):
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        todo_object=Task.objects.get(id=id)
        form_instance=TaskForm(instance=todo_object)
        return render(request, "todo_edit.html", {"form":form_instance})
    def post(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        todo_object=Task.objects.get(id=id)
        form_instance=TaskForm(request.POST,instance=todo_object)
        if form_instance.is_valid():
            
            form_instance.save()
            return redirect("todo-list")
        return render(request, "todo_edit.html", {"form":form_instance})

@method_decorator(auth_required, name="dispatch")   
class ToDoDeleteView(View):
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        Task.objects.get(id=id).delete()
        return redirect("todo-list")
        
        
        
        

        
        
        
        
        
        
        
        