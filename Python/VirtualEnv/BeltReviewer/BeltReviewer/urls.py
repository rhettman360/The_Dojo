from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
    url(r'^', include('apps.login.urls', namespace='login')),
    url(r'^books/', include('apps.review.urls', namespace='review'))
]
