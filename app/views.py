from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
# Home Page
class IndexListView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    def get(self,request):
        return Response('HelloWorld')       
