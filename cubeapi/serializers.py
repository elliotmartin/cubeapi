from rest_framework import serializers
from django.contrib.auth.models import User
from cubeapi.models import Cube, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')
        
class CubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cube
        fields = ('id', 'cube_id', 'cube', 'created')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')