from django.shortcuts import render, HttpResponse
from datetime import datetime

def show_time(request):
    now = datetime.now()
    print(now)
    context = {
        "current_time": now,
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"],
        "my_list": ["Sam", "Pal", "Pam"]
    }
    return render(request, "index.html", context)

