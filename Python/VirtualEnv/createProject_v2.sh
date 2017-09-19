#!/bin/bash

echo What is your project name?
read project
echo What is your app name?
read app
echo What is your page name?
echo TYPE ^ IF NO NAME
echo OTHERWISE ADD A FORWARD SLASH AT THE END OF THE NAME
read page

django-admin startproject $project
cd $project

cd $project
rm -f urls.py

echo "from django.conf.urls import url, include" >> urls.py
echo "from django.contrib import admin" >> urls.py
echo "urlpatterns = [" >> urls.py
echo "    url(r'^admin/', admin.site.urls)," >> urls.py
echo "    url(r'$page', include('apps.$app.urls'))," >> urls.py
echo "]" >> urls.py
cd ..

mkdir apps
cd apps
echo >__init__.py

django-admin startapp $app
cd $app

echo "from django.conf.urls import url" >> urls.py
echo "from django.contrib import admin" >> urls.py
echo "from . import views" >> urls.py
echo "urlpatterns = [" >> urls.py
echo "    url(r'^$', views.index)," >> urls.py
echo "]" >> urls.py

rm -f views.py
echo "from django.shortcuts import render" >> views.py
echo "def index(request):" >> views.py
echo "    return render(request, '$app/index.html') #end" >> views.py

mkdir templates

cd templates
mkdir $app
cd $app
echo > index.html
read -p "All done, make sure to add 'apps.[app_name]', to the settings file! Enter to continue."
