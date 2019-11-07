from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


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
