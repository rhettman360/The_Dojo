from django.shortcuts import render

def index(request):
    return render(request, 'main_app/index.html')

def submit(request):
    content={
    "name":request.POST['name'],
    }
    return render(request, "main_app/result.html", content)
