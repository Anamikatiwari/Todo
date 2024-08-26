from django.contrib import admin
from django.urls import path, include
from app.views import home, login, signup, add_todo


urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    z
    path('add-todo/', add_todo, name='add-todo'),
    
]
