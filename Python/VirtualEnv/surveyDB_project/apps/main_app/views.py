from django.shortcuts import render, redirect
from models import User

def index(request):
    context = {
        'users': User.objects.all()
    }

    return render(request, 'main_app/index.html', context)

def process(request):
    User.objects.create(name = request.POST['first_name'])
    return redirect('/')

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/')
