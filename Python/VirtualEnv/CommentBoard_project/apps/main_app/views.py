from django.shortcuts import render, redirect
from django.contrib import messages
from models import Comment

def index(request):

    context = {
        'comments': Comment.objects.all().order_by('-created_at'),
    }
    return render(request, 'main_app/index.html', context)

def process(request):
    results = Comment.objects.validate(request.POST)
    if results['status'] == True:
        value = Comment.objects.creator(request.POST)
    else:
        for error in results['errors']:
            messages.error(request, error)

    return redirect('/')
