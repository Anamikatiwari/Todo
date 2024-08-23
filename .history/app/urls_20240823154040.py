from django.contrib import admin
from django.urls import path, include
from app.views import home, loginogin


urlpatterns = [
    path('', home),
    path('login', login),
]
