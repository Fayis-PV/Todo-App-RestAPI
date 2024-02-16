from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.response import Response
from rest_framework import status

# Create your models here.
class CustomUser(AbstractUser):
    # make email unique and username not unique but required
    email = models.EmailField(unique = True)
    username = models.CharField(max_length=100, unique = False, validators = [])
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username
    
    
    # check unique username on signup
    def check_username(self,username):
        try:
            user = CustomUser.objects.get(username = username)
            print(user.username)
            return Response({'username': 'Username already exists'}, status = status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return True
        
    def check_email(self,email):
        try:
            user = CustomUser.objects.get(email = email)
            return Response({'email': 'Email already exists'}, status = status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return True
    
    
    def get_username(self,email):
        user = CustomUser.objects.get(email = email)
        return user.username
    

class Todo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = 'todos')
    title = models.CharField(max_length=100)
    email = models.EmailField()
    start = models.DateTimeField(auto_now=False, auto_now_add=False, null = True, blank = True)
    end = models.DateTimeField(auto_now=False, auto_now_add=False, null = True, blank = True)
    location = models.CharField(max_length=500, null = True, blank = True)
    notes = models.TextField(null = True, blank = True)
    inform_before = models.IntegerField(default = 10)
    completed = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    
    
