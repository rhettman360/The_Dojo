from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^results$', views.submitter),
    url(r'^checkout$', views.checkout),
    url(r'^clear$', views.clear),
]
