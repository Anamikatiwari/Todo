from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world!")


urlpatterns = [
    path('', home)
]
