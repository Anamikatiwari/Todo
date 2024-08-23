from django.contrib import admin
from django.urls import path, include

def home(request):
    return HttpResponse("Hello, world!")