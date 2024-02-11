from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Todo, CustomUser
from .serializers import TodoSerializer
from rest_framework import status


# Create your views here.
# Home Page
class TodoListView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        customuser = CustomUser
        todo = Todo.objects.filter(user = user)
        return todo

class TodoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer