from django.shortcuts import render
from .models import Author

def index(request):
    context = {"authors": Author.objects.all()}	
    return render(request, "index.html", context)
