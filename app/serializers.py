from rest_framework import serializers
from .models import Todo

# Create Here serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields ='__all__'