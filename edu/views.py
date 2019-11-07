from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from edu.forms import *


def home(request):
    return render(request, 'home.html')


def register(request):
    invalidPassword = False
    invalidUsername = False
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edu:home')
        else:
            if request.POST['password1'] != request.POST['password2']:
                invalidPassword = True
            if User.objects.filter(username=request.POST.get('username')).exists():
                invalidUsername = True
            return render(request, 'register.html',
                          {'form': form, 'invalidUsername': invalidUsername, 'invalidPassword': invalidPassword})
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/', {'user': user})
        else:
            return redirect('/', {'error': True})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout(requset):
    pass
