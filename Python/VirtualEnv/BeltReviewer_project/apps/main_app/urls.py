from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^books$', views.books),
    url(r'^logout$', views.logout),
]
