from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    html = '''
        <h1>Home Page</h1>
        <ul>
            <li>I</li>
        </ul>
    
    '''
    return HttpResponse("Hello, world!")