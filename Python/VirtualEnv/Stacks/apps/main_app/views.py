from django.shortcuts import render, redirect

def index(request):
    if "stack" not in request.session.keys():
        request.session['stack'] = []
    return render(request, 'main_app/index.html') #end

def add(request):
    sessionlist = request.session['stack']
    sessionlist.append(int(request.POST['value']))
    request.session['stack'] = sessionlist
    return redirect('/')

def remove(request):
    sessionlist = request.session['stack']
    sessionlist.pop()
    request.session['stack'] = sessionlist
    return redirect('/')
