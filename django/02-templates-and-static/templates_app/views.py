from django.shortcuts import render, HttpResponse

    
def index(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"],
        "my_list": ["Sam", "Pal", "Pam"]
    }
    return render(request, "index.html", context)

