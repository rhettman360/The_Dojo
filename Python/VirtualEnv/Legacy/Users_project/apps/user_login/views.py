from django.shortcuts import render
def index(request):
    return render(request, 'user_login/index.html') #end
