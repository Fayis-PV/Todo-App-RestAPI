from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Todo, CustomUser
from .serializers import TodoSerializer
from rest_framework import status
from allauth.account.views import ConfirmEmailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.permissions import AllowAny
from datetime import timedelta
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# Create your views here.

class CustomConfirmEmailView(ConfirmEmailView):
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)
        return HttpResponseRedirect('/auth/login/')  # Redirect to a custom URL after email verification

# Home Page
class TodoListCreateView(APIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        try:
            user = self.request.user
            todo = Todo.objects.filter(user = user)
            return todo
        except Todo.DoesNotExist:
            return Response({'Not Found: Todo is not found'},status = status.HTTP_404_NOT_FOUND)
        except CustomUser.DoesNotExist:
            return Response({'Not Found: User is not found'}, status = status.HTTP_404_NOT_FOUND)
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            data = self.get_queryset()
            serializer = TodoSerializer(data, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return HttpResponseRedirect(reverse('rest_login'))
    
    def post(self, request):
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = self.request.user)
            return HttpResponseRedirect(reverse('home'))
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class TodoDetailView(APIView):

    @property
    def allowed_methods(self):
        return ['GET', 'PUT', 'DELETE']

    def get(self, request, pk, *args, **kwargs):
        try:
            todo = Todo.objects.get(id = pk)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Todo.DoesNotExist:
            return Response({'Not Found': 'Todo is not found '}, status = status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, *args, **kwargs):
        todo = Todo.objects.get(id = pk)
        serializer = TodoSerializer(todo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        todo = Todo.objects.get(id = pk)
        todo.delete()
        return HttpResponseRedirect(reverse('home'))


class TodoCompleteView(APIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def post(self, request, pk, *args, **kwargs):
        todo = Todo.objects.get(id = pk)
        if todo.user == request.user:
            todo.completed = True
            todo.save()
        else:
            return Response(status = status.HTTP_403_FORBIDDEN)
        return HttpResponseRedirect(reverse('home'))
    
    
class TodoIncompleteView(APIView):
        queryset = Todo.objects.all()
        serializer_class = TodoSerializer

        def post(self, request, pk, *args, **kwargs):
            todo = Todo.objects.get(id=pk)
            if todo.user == request.user:
                todo.completed = False
                todo.save()
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
            return HttpResponseRedirect(reverse('home'))
        
