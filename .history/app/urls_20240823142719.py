from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from. import ho


urlpatterns = [
    path('', home)
]
