from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from. view import home


urlpatterns = [
    path('', home)
]
