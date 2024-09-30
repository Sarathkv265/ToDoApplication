from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    
    title = models.CharField(max_length=200)
    
    created_date = models.DateTimeField(auto_now=True,null=True)
    
    Due_date = models.DateTimeField(null=True)
    

    
    task_status = models.BooleanField(default=False)
    
    discription = models.TextField(null=True)
    
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        unique_together=("title","owner")
        
    def __str__(self):
        
        return self.title
    