from django.shortcuts import render
# import  Todo Model 
from api.models import Todo
# import TodoSerializer
from api.serializers import TodoSerialzer 
# import viewsets and permissions
from rest_framework import viewsets
 
#create class base view 

class TodoViewSet(viewsets.ModelViewSet):
    queryset  = Todo.objects.all() 
    serializer_class = TodoSerialzer
    
    



