from django.shortcuts import render, HttpResponse
def surveys(request):
    response = "placeholder to later display all the list of created surveys"
    return HttpResponse(response)

def new(request):
    response = "placeholder for users to add a new survey"
    return HttpResponse(response)
