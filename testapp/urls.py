from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('about',about_attempt, name="about_attempt"),
    path('skills',skills_attempt, name="skills_attempt"),
    path('home',home_attempt, name="home_attempt"),
    path('about',about_attempt_again, name="about_attempt_again"),
    path('work',work_attempt, name="work_attempt"),
    path('work',work_attempt_again, name="work_attempt_again"),
    path('home',home_attempt_again, name="home_attempt_again"),
    path('contact',contact_attempt,name="contact_attempt"),
    path('contact',contact_attempt_again,name='contact_attempt_again')
]
