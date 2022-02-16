from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Userview(generics.ListAPIView):
    permission_class=[IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()