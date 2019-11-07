from django.contrib import admin
from django.urls import path
from edu.views import *

app_name = 'edu'
urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]
