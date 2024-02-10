from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.
# Home Page
class TodoListView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer