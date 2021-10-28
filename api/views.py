from django.shortcuts import render
from rest_framework import viewsets

from django.http import HttpResponse
import json

from api.serializer import FoodSerializer, GroupSerializer, UserSerializer

from .models import FoodModel, GroupModel, UserModel

# Create your views here.


class FoodViewSet(viewsets.ModelViewSet):
    queryset = FoodModel.objects.all()
    serializer_class = FoodSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer
