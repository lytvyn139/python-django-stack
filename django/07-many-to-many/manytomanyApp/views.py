from django.shortcuts import render
from .models import *

def index(request):
    context = {
        "books": Book.objects.all(),
        "publishers": Publisher.objects.all()
        }	
    return render(request, "index.html", context)
