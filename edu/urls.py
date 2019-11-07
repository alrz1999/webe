from django.contrib import admin
from django.urls import path
from edu.views import *





urlpatterns = [
    path('', home, name='home'),
    path('register', signup, name='signup'),
    path('signin', signin, name='signin'),
    # path('logout',logout,name = 'logout')
]
