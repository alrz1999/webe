from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from edu.views import *

app_name = 'edu'
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/$', log_in, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^cotactus/$', contact_us, name='contact_us')
]
