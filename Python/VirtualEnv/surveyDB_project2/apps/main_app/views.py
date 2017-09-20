from django.shortcuts import render, redirect
from models import User

def index(request):
    return render(request, 'main_app/index.html')

def process(request):
    User.objects.create(name = request.POST['name'])
    return redirect('/')

def all(request):
        context = {
            'users': User.objects.all()
        }
        return render(request, 'main_app/return.html', context)

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/all')
