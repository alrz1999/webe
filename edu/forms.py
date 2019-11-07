from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label='نام')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label='نام خانوادگی')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', label='ایمیل')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', ]


class SignInForm(ModelForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password',)
