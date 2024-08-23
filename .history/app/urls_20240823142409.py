from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    print("Hello World!...this is home")
    return HttpResponse("Hello, world!")


urlpatterns = [
    path('', home)
]
