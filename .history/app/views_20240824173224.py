from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
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
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth(request, user)  # Log the user in
                return redirect('home')  # Redirect to the homepage or another appropriate view
            else:
                context = {
                    'form': form,
                    'error': 'Invalid login credentials'
                }
                return render(request, 'login.html', context=context)
        else:
            context = {
                'form': form
            }
            return render(request, 'login.html', context=context)
                



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
