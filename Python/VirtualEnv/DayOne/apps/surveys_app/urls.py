from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'main', views.surveys),
    url(r'new', views.new),
]
