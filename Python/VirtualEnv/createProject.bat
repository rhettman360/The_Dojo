@echo off
set /p project= What is your project name?
set /p app= What is your app name?
set /p page= What is your page name? LEAVE BLANK IF NO NAME, OTHERWISE ADD A FORWARD SLASH AT THE END OF THE NAME

@echo on
django-admin startproject %project%
cd %project%

cd %project%
del urls.py

@echo off
echo from django.conf.urls import url, include>>urls.py
echo from django.contrib import admin>>urls.py
echo urlpatterns = [>>urls.py
echo     url(r'^admin/', admin.site.urls),>>urls.py
echo     url(r'^%page%', include('apps.%app%.urls')),>>urls.py
echo ]>>urls.py
cd ..

@echo on
mkdir apps
cd apps
echo.>__init__.py

timeout 2
django-admin startapp %app%
cd %app%

@echo off
echo from django.conf.urls import url>>urls.py
echo from django.contrib import admin>>urls.py
echo from . import views>>urls.py
echo urlpatterns = [>>urls.py
echo     url(r'^$', views.index),>>urls.py
echo ]>>urls.py

del views.py
echo from django.shortcuts import render>>views.py
echo def index(request):>>views.py
echo     return render(request, '%app%/index.html') #end >> views.py

mkdir templates

cd templates
mkdir %app%
cd %app%
echo.> index.html
echo ""
echo ""
echo "All done, make sure to add 'apps.[app_name]', to the settings file! Enter to continue."
pause
