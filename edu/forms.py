from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

from edu.models import ContactUs, Course, UserProfile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label='first name')
    last_name = forms.CharField(max_length=30, required=False, label='last name')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', label='email')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', ]

    # can add more rules but can not deacrease them
    # def is_valid(self):
    #     super().is_valid()
    #     if self.data['password2'] == self.data['password1']:
    #         return True


class LoginForm(ModelForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password',)


class ContactUsForm(ModelForm):
    title = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    text = forms.CharField(widget=forms.Textarea, max_length=250, min_length=10, required=True)

    class Meta:
        model = ContactUs
        fields = ['title', 'text', 'email']


class ProfileSettingForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    profile_image = forms.ImageField(required=False, )


class MakeNewCourseForm(ModelForm):
    exam_time = forms.DateField(required=True)

    class Meta:
        model = Course
        fields = ('department', 'name', 'course_number', 'group_number', 'teacher', 'start_time', 'end_time',
                  'first_day', 'second_day', 'exam_date')



class SearchForm(ModelForm):
    class Meta:
        model = Course
        fields = ('department',)
