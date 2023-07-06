from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Creating a todo model to store data 

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    completed = models.BooleanField(default=False)
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title