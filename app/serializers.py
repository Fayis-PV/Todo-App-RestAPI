from rest_framework import serializers
from .models import Todo

# Create Here serializers
min_choices = (
    (0 , 'Don\'t inform me'),
    (1 , '1 Minute before'),
    (2 , '2 Minutes before'),
    (3 , '3 Minutes before'),
    (5 , '5 Minutes before'),
    (10, '10 Minutes before'),
    (15, '15 Minutes before'),
    (30, '30 Minutes before'),
    (60, '1 Hour before')
)

# Create your serializers here.
# set email as user email and not to be editable
class TodoSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only = True)
    user = serializers.CharField(read_only= True)
    inform_before = serializers.ChoiceField(choices = min_choices)
    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ['email']
    
    def create(self, validated_data):
        validated_data['email'] = self.context['request'].user.email
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    