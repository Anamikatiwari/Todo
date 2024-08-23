from django.contrib import admin
from django.urls import path, include

def home(request):
    print
    return HttpResponse("Hello, world!")