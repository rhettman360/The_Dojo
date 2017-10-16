# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from ..login_app.models import User
from django.contrib import messages

def index(request):
    # print request.session['user_id']
    if "email" not in request.session.keys():
        return redirect('/')
    else:
        user_id = request.session['user_id']
        context = {
            'count': User.objects.get(id = user_id).counter,
            'otherUsers': User.objects.exclude(id = user_id),
        }
        return render(request, 'main_app/index.html', context)

def five(request, userid):
    if "email" not in request.session.keys():
        return redirect('/')
    else:
        a = User.objects.get(id = userid)
        a.counter = a.counter + 1
        a.save()
        return redirect('/main')
