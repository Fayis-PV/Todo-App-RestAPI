from rest_framework.serializers import Serializer
from .models import Todo

# Create Here serializers

class TodoSerializer(Serializer):
    class Meta:
        model = Todo