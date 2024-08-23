from django.contrib import admin
from django.urls import path, include
from app.views import home, login


urlpatterns = [
    path('', home),
    path('login', login),
]
