from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField()
    start = models.DateTimeField(auto_now=False, auto_now_add=False, null = True, blank = True)
    end = models.DateTimeField(auto_now=False, auto_now_add=False, null = True, blank = True)
    location = models.CharField(max_length=500, null = True, blank = True)
    notes = models.TextField(null = True, blank = True)
    inform_before = models.IntegerField(default = 10)

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    
    
