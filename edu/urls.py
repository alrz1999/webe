from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from edu.views import *

app_name = 'edu'
urlpatterns = [
    path('', home, name='home'),
    path('login/', log_in, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout_view'),
    path('cotactus/', contact_us, name='contact_us'),
    path('profileview/', profile_view, name='profileView'),
    path('panelview/', panel_view, name='panelview'),
    path('setting/', profile_setting_view, name='profileSettingView'),
    path('makenewcourse', make_new_course, name='make_new_course'),
    path('coursesview', courses_view, name='coursesView')
]
