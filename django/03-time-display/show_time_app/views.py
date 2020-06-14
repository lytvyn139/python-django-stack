from django.shortcuts import render, HttpResponse
from datetime import datetime

def show_time(request):
    now = datetime.now()
    print(now)
    context = {
        'current_time': now
    }

    return render(request, "index.html", context)

