from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from cubeapi.serializers import UserSerializer, CubeSerializer, CategorySerializer
from django.contrib.auth.models import User
from cubeapi.models import Cube, Category

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class CubeViewSet(viewsets.ModelViewSet):
    queryset = Cube.objects.all()
    serializer_class = CubeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer