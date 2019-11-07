from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from edu.forms import *


def home(request):
    return render(request, 'home.html')


def signup(request):
    truePassword = True
    trueUsername = True
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            if request.POST['password1'] != request.POST['password2']:
                truePassword = False
            elif len(User.objects.all().filter(username=request.POST['username'])) > 0:
                trueUsername = False
            return redirect('/register', {'form': form, 'truePassword': truePassword, 'trueUsername': trueUsername})
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
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
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})
