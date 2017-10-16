from django.shortcuts import render, redirect

from models import User

def index(request):
    context={
        'users' : User.objects.all()
    }

    return render(request, 'main_app/index.html',context) #end

def new(request):
    return render(request, 'main_app/create.html')

def show(request,userid):
    context={
        "users" : User.objects.get(id=userid)
    }    
    return render(request, 'main_app/show.html',context)

def edit(request,userid):
    context={
        "users" : User.objects.get(id=userid)
    }    
    return render(request, 'main_app/edit.html',context)

def update(request,userid):
    url="/users/" + userid +"/"
    user = User.objects.get(id=userid)
    user.full_name = request.POST['full_name']
    user.email = request.POST['email']
    user.save()
    print user.full_name
    print user.email
    print User.objects.get(id=userid).full_name
    return redirect(url)

def delete(request, userid):
    url='/users/'
    User.objects.get(id=userid).delete()
    return redirect(url)

def create(request):
    url='/users/'
    User.objects.create(full_name=request.POST['full_name'], email=request.POST['email'])
    return redirect(url)