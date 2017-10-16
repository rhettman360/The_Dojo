from django.shortcuts import render,redirect
from models import *

def index(request):
    return render(request, 'main_app/index.html')

def process(request):
    if request.POST['animal'] == "Cats":
        Cat.objects.create(name = request.POST['name'])
    else:
        Dog.objects.create(name = request.POST['name'])
    return redirect('/')

def all(request):
        context = {
            'cats': Cat.objects.all(),
            'dogs': Dog.objects.all(),
        }
        return render(request, 'main_app/return.html', context)
