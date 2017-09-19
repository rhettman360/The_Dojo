from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'main', views.blog),
    url(r'new', views.new),
    url(r'create', views.create),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/edit', views.edit),
    url(r'^(?P<number>\d+)/delete', views.delete),
]
