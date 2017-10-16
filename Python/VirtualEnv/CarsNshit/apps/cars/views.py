# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from ..login.models import User
from models import Car
from django.contrib import messages

def index(request):
    # print request.session['user_id']
    if "email" not in request.session.keys():
        return redirect('/')
    else:
        user_id = request.session['user_id']
        context = {
            'userCars': User.objects.get(id = request.session['user_id']).cars.all(),
            'otherUsers': User.objects.exclude(id = request.session['user_id']),
        }
        return render(request, 'cars/index.html', context)

def create(request):
    postData = request.POST
    results = {'status': True, 'errors': []}
    if len(postData['year']) < 1 or len(postData['year']) > 4:
        results['errors'].append('Year must be 4 digits long')
        results['status'] = False
    if len(postData['make']) < 1:
        results['errors'].append('Try typing something dumbass')
        results['status'] = False
    if len(postData['model']) < 1:
        results['errors'].append('Try typing something dumbass')
        results['status'] = False
    if results['status'] == True:
        c = Car(make = postData['make'], model = postData['model'], year = postData['year'])
        c.save()
        c.driver.add(User.objects.get(id = request.session['user_id']))
        return redirect('/cars')
    else:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/cars/add')


def add(request):
    if "email" not in request.session.keys():
        return redirect('/')
    else:
        return render(request, 'cars/add.html')
    return redirect('/cars')

def show(request, userid):
    if "email" not in request.session.keys():
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=userid)
        }
        return render(request, 'cars/show.html', context)
