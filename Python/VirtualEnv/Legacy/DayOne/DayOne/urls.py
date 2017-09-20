from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'blogs/', include('apps.blogs_app.urls')),
    url(r'surveys/', include('apps.surveys_app.urls')),
    url(r'users/', include('apps.users_app.urls')),
]
