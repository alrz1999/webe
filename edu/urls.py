from django.contrib import admin
from django.urls import path
from edu.views import *

app_name = 'edu'
urlpatterns = [
    path('', home, name='home'),
    path('register', sign_up, name='sign_up'),
    path('signIn', sign_in, name='sign_in'),
    path('logout', log_out, name='log_out')
]
