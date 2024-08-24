from django.contrib import admin
from django.urls import path, include
from app.views import home, login, signup


urlpatterns = [
    path('', home, name='home'),
    path('login/', login, ),
    path('signup/', signup)
]
