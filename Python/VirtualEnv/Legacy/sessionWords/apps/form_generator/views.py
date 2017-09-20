from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
    if "counter" not in request.session.keys():
        request.session['counter'] = 0
    if "formstring" not in request.session.keys():
        request.session['formstring'] = ""
    return render(request, "form_generator/index.html")

def submitter(request):
    request.session['counter'] += 1
    if 'size' not in request.POST:
        textsize = '5'
    else:
        textsize = request.POST['size']
    formstring = str("<h2 class='" + request.POST['color'] + " text-darken-2'><font size='" + textsize + "'>" + request.POST['name'] + "</font></h2>")
    print formstring
    request.session['formstring'] += formstring
    context = {
    "formstring": request.session['formstring'],
    }
    # print request.session['formstring']
    return render(request, "form_generator/index.html", context)

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    if "counter" not in request.session.keys():
        request.session['counter'] = 0
    if "formstring" not in request.session.keys():
        request.session['formstring'] = ""
    return render(request, "form_generator/index.html")
