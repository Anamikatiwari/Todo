from django.contrib import admin
from django.urls import path, include

def home(request):
    print("Hello World!...this is home")
    return HttpResponse("Hello, world!")


urlpatterns = [
    path('', )
]
