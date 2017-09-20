from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^all$', views.all),
    url(r'^delete/(?P<user_id>[0-9]+)$', views.delete)
]
