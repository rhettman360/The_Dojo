from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
    url(r'^', include('apps.login_app.urls')),
    url(r'main/', include('apps.main_app.urls')),
]
