from django.shortcuts import render, redirect
from time import strftime, strptime
from . models import Show

    # ROUTE 1
def index(request): 
    Show.objects.all()
    context = {
        'new_show': Show.objects.all()
    }
    return render(request, 'index.html', context)

    # ROUTE 2
def create_show(request): 
    new_show = Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        desc=request.POST['desc']
    )
    return redirect(f'/shows/{new_show.id}')

    # ROUTE 3
def show_info(request, show_id):
    selected_show = Show.objects.get(id=show_id)
    context = {
        'selected_show': selected_show
    }
    return render(request, 'show_info.html', context)

########################################################
#   3 options route => show_info.html 
    # ROUTE 4
def all_shows(request):
    all_shows = Show.objects.all()
    context = {
        'all_shows': all_shows
    }
    return render(request, 'all_shows.html', context)

    # ROUTE 5
#GET REQUEST
def edit_show(request, show_id):
    selected_show = Show.objects.get(id=show_id)
    context = {
        'selected_show': selected_show
    }
    return render(request, 'edit_show.html', context)

    # ROUTE 6
#GET REQUEST
def delete_show(request, show_id):
    selected_show = Show.objects.get(id=show_id)
    selected_show.delete()
    return redirect('/shows')  #redirects to /shows after deleting
    
########################################################
# POST REQUEST
def update_show(request, show_id):
    print(request.POST)
    show_to_update = Show.objects.get(id=show_id)
    show_to_update.title = request.POST['title']
    show_to_update.network = request.POST['network']
    show_to_update.release_date = request.POST['release_date']
    show_to_update.desc = request.POST['desc']
    show_to_update.save()
    return redirect(f'/shows/{show_id}')


def new_show(request):
    return redirect('/')




