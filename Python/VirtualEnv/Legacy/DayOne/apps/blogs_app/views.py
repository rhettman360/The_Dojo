from django.shortcuts import render, HttpResponse, redirect
def blog(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('./main/')

def show(request, number):
    response = "placeholder to display blog ", number
    return HttpResponse(response)

def edit(request, number):
    response = "placeholder to edit blog ", number
    return HttpResponse(response)

def delete(request, number):
    response = "placeholder to delete blog ", number
    return HttpResponse(response)
