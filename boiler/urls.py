from urllib.parse import urlparse
from django.urls import path
from .views import *

urlpatterns=[
    path('birthdays/',BirthdaysAPI.as_view(), name='birthday'),
    path('birthdays/<int:id>',BirthdaysUpdateDelAPI.as_view(), name='single-birthday'),
]