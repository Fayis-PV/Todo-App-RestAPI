from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField()
    start = models.DateTimeField(auto_now=False, auto_now_add=False, null = True, blank = True)
    end = models.DateTimeField(auto_now=False, auto_now_add=False, null = True, blank = True)
    location = models.CharField(max_length=500)
    notes = models.TextField()
    inform_before = models.BooleanField()

