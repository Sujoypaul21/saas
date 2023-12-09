from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class EmployeeListView(generics.ListAPIView):
    queryset = User.objects.filter(is_employee=True)
    serializer_class = UserSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_employee=True)
    serializer_class = UserSerializer

# Create your views here.
