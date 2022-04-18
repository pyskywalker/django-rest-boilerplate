from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Birthdays
from .serializers import BirthdaySerializer
# Create your views here.

class BirthdaysAPI(generics.ListCreateAPIView):
    permission_classes = [AllowAny,]
    queryset=Birthdays.objects.all()
    serializer_class=BirthdaySerializer

class BirthdaysUpdateDelAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny,]
    queryset=Birthdays.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class=BirthdaySerializer