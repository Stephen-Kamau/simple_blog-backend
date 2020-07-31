from .models import Todo
from rest_framework import serializers




class Todoserial(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


        
