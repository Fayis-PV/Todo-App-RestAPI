from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView,RetrieveAPIView
from .models import Todo, CustomUser
from .serializers import TodoSerializer
from rest_framework import status
from allauth.account.views import ConfirmEmailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.permissions import AllowAny

# Create your views here.

class CustomConfirmEmailView(ConfirmEmailView):
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)
        return HttpResponseRedirect('/auth/login/')  # Redirect to a custom URL after email verification

# Home Page
class TodoListView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        todo = Todo.objects.filter(user = user)
        return todo

class TodoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoCompleteView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, pk, *args, **kwargs):
        todo = Todo.objects.get(id = pk)
        if todo.user == request.user:
            todo.completed = True
            todo.save()
        else:
            return Response(status = status.HTTP_403_FORBIDDEN)
        return HttpResponseRedirect(reverse('home'))
    
class TodoDeleteView(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def delete(self, request, pk, *args, **kwargs):
        todo = Todo.objects.get(id = pk)
        if todo.user == request.user:
            todo.delete()
        else:
            return Response(status = status.HTTP_403_FORBIDDEN)
        return HttpResponseRedirect(reverse('home'))
    
class TodoIncompleteView(RetrieveAPIView):
        queryset = Todo.objects.all()
        serializer_class = TodoSerializer

        def get(self, request, pk, *args, **kwargs):
            todo = Todo.objects.get(id=pk)
            if todo.user == request.user:
                todo.completed = False
                todo.save()
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
            return HttpResponseRedirect(reverse('home'))


