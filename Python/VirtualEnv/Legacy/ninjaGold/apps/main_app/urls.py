from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^farm$', views.farm),
    url(r'^cave$', views.cave),
    url(r'^house$', views.house),
    url(r'^casino$', views.casino),
    url(r'^clear$', views.clear),
]
