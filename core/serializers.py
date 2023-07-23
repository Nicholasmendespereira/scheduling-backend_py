from rest_framework import serializers
from .models import Usuario

# create a sereliazer class
class TodoSerializer(serializers.ModelSerializer):
  
    # create a meta class
    class Meta:
        model = Usuario
        fields = ['id', 'name']