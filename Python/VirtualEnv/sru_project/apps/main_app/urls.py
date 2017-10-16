from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^(?P<userid>\d+)/update/$', views.update),
    url(r'^(?P<userid>\d+)/$', views.show),
    url(r'^create/$', views.create),
    url(r'^(?P<userid>\d+)/edit$', views.edit),
    url(r'^(?P<userid>\d+)/delete$', views.delete),

]
