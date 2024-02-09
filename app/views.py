from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status

# Create your views here.
# Home Page
class IndexListView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    def get(self,request):
        data = self.queryset
        print(data)
        return Response(data=data,status=status.HTTP_200_OK)   
