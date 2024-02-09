from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView,ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Todo


# Create your views here.
# Home Page
class IndexListView(ListAPIView):
    def get(self,request):
        pass