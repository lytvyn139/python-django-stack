from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] +=1
    random_chars = get_random_string(length=14)
    print(random_chars)
    context = {
        'random_words_from_py': random_chars
    }
    return render(request, "home.html", context)

def reset(request):
    del request.session['counter']
    return redirect("/random_word")

def process(request):
    print(request.POST)
    return redirect("/random_word")
