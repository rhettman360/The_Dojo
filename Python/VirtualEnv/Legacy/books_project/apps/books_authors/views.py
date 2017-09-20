from django.shortcuts import render
def index(request):
    return render(request, 'books_authors/index.html') #end
