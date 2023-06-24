from django.shortcuts import render
from rest_framework import generics
from .serializers import ToDoSerializer
from.models import ToDo

# Create your views here.

class ListToDo(generics.ListAPIView):   # read && create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class CreateToDo(generics.CreateAPIView):   # create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailToDo(generics.RetrieveUpdateDestroyAPIView):   # update && delete
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

# class DeleteToDo(generics.DestroyAPIView):   # delete
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
