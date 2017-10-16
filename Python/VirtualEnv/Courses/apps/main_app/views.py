from django.shortcuts import render, HttpResponse, redirect
from .models import Course

def index(request):
    context={
        'courses' : Course.objects.all()
    }
    return render(request, 'main_app/index.html', context)

def add(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        # for tag, error in errors.iteritems():
        #     messages.error(request, error, extra_tags=tag)
        return redirect('/youdunfuckedup')
    else:
        url='/'
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
        return redirect(url)

def fuckedup(request):
    return HttpResponse('Try again dumbass')

def areyousure(request,courseid):
    context={
        'courses' : Course.objects.get(id=courseid)
    }
    return render(request, "main_app/areyousure.html", context)

def delete(request, courseid):
    url='/'
    Course.objects.get(id=courseid).delete()
    return redirect(url)
