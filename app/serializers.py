from rest_framework import serializers
from .models import Todo

# Create Here serializers
min_choices = (
    (0 , 'Don\'t inform'),
    (1 , '1 Minute before'),
    (2 , '2 Minutes before'),
    (3 , '3 Minutes before'),
    (5 , '5 Minutes before'),
    (10, '10 Minutes before'),
    (15, '15 Minutes before'),
    (30, '30 Minutes before'),
    (60, '1 Hour before')
)

class TodoSerializer(serializers.ModelSerializer):
    inform_before = serializers.ChoiceField(min_choices)
    class Meta:
        model = Todo
        fields ='__all__'