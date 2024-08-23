from django.contrib import admin
from django.urls import path, include
from app.views import home, ogin


urlpatterns = [
    path('', home),
    path('login', login),
]
