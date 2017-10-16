from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^(?P<courseid>\d+)/delete$', views.delete),
    url(r'^(?P<courseid>\d+)/areyousure$', views.areyousure),
    url(r'^youdunfuckedup$', views.fuckedup),
]
