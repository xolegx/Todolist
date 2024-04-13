from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from  first.serializers import CreateUserSerializer

class SignupView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
