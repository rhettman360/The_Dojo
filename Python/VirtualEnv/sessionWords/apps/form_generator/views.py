from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    if "maths" not in request.session.keys():
        request.session['maths'] = 0
    return render(request, "form_generator/index.html")

def submitter(request):
    if request.POST['num1'].isalpha() == True or request.POST['num2'].isalpha() == True:
        messages.error(request, "No letters allowed!")
        return redirect('/')
    else:
        request.session['maths'] = int(request.POST['num1']) + int(request.POST['num2'])
        context = {
        "maths": request.session['maths'],
        }
        return render(request, "form_generator/result.html", context)

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    if "maths" not in request.session.keys():
        request.session['maths'] = ""
    return render(request, "form_generator/index.html")
