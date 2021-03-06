from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
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


def log_in(request):
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


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                request.POST['title'],
                request.POST['text'] + '\n' + request.POST['email'],
                'ababaei037@gmail.com',
                ['webe19lopers@gmail.com', ],
            )
            return render(request, 'aftercontactUs.html')
        else:
            return redirect('edu:contact_us')

    form = ContactUsForm()
    return render(request, 'contactus.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login')
def profile_view(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


def panel_view(request):
    return render(request, 'panel.html', {'user': request.user})


def profile_setting_view(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        user = request.user
        if firstname != '':
            user.first_name = firstname
        if lastname != '':
            user.last_name = lastname
        if request.FILES.get('profile_image'):
            user.userprofile.profile_image = request.FILES['profile_image']
            user.userprofile.save()
        user.save()
        return render(request, 'profile.html', {'user': user})
    else:
        form = ProfileSettingForm()
    return render(request, 'profilesetting.html', {'form': form})


def make_new_course(request):
    if request.method == 'POST':
        form = MakeNewCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'makenewcourse.html', {'form': form})
        return render(request, 'makenewcourse.html', {'form': form})
    form = MakeNewCourseForm()
    return render(request, 'makenewcourse.html', {'form': form})


def courses_view(request):
    return render(request, 'courses.html', {'courses': Course.objects.all()})


def search_course(request):
    coursess = []
    if request.POST:

        name = request.POST['search_query']
        dcheck = request.POST.get('department')
        tcheck = request.POST.get('teacher')
        ccheck = request.POST.get('course')
        print(name)
        if (not dcheck and not tcheck and not ccheck) or dcheck:
            for course in Course.objects.all():
                if course.department == name:
                    coursess.append(course)
        if tcheck:
            for course in Course.objects.all():
                if course.teacher == name:
                    coursess.append(course)
        if ccheck:
            for course in Course.objects.all():
                if course.name == name:
                    coursess.append(course)
        coursess = list(dict.fromkeys(coursess))

        # records = []
        # for course in Course.objects.filter(department=department1):
        #     records.append(course)
        # results = records

        return render(request, 'courses.html', {'coursess': coursess, 'courses': Course.objects.all()})
    return render(request, 'courses.html', {'coursess': coursess, 'courses': Course.objects.all()})


def add_course(request):
    pass
