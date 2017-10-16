from django.shortcuts import render,redirect
from models import User
from django.contrib import messages

def index(request):
    return render(request, 'main_app/index.html')

def process(request):
    results = User.objects.validate(request.POST)
    if results['status'] == True:
        user = User.objects.creator(request.POST)
        messages.success(request, 'You are successfully registered!')
    else:
        for error in results['errors']:
            messages.error(request, error)

    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        messages.error(request, 'u dun fucc')
        return redirect('/')
    request.session['email'] = results['user'].email
    request.session['first_name'] = results['user'].first_name
    return redirect('/dashboard')

def logout(request):
    request.session.flush()
    return redirect('/')

def dashboard(request):
    return render(request, 'main_app/dashboard.html')
