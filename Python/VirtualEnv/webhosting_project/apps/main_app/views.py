from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

def index(request):
    return render(request, 'main_app/index.html')

def checking(request):
    for sites in Site.objects.all():
        if request.POST['url'] == sites.url:
            messages.error(request, "Your name isn't avaliable")
            return redirect('/')
        else:
            messages.error(request, "Your name is avaliable!")
            return redirect('/')
    if Site.objects.all().count() == 0:
        messages.error(request, "There are no sites in the DB")
        return redirect('/')

def result(request):
    context={
        'urls':Site.objects.all()
    }
    return render(request, 'main_app/result.html', context)

def process(request):
    Site.objects.create(url=request.POST['url'])
    return redirect('/result')
