from django.contrib import admin
from django.urls import path, include
from app.views import home, login, signup, add_todo, signout


urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('add-todo/', add_todo, name='add-todo'),
    path('logout/', signout, name='signup'),
    
]
