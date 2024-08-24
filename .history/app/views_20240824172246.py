from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import au
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            



def signup(request):
    
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'signup.html', context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            user = form.save()
            print('User created:', user)
            if user is not None:
                return redirect('login')  
        else:
            print('Form is not valid')
            return render(request, 'signup.html', context=context)
