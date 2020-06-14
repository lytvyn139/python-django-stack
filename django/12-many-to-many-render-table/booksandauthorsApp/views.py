from django.shortcuts import render, HttpResponse, redirect
from . models import Book, Author

def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'index.html', context)

