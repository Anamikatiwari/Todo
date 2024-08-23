from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    html = '''
        <h1>Home Page</h1>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
            <li>Item 4</li>
        </ul>
        <button></button
    
    '''
    return HttpResponse(html)