from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'register', views.register),
    url(r'login', views.login),
    url(r'users/new', views.register),
    url(r'users', views.users),
]
