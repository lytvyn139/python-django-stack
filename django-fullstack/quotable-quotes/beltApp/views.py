from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='register') 
        return redirect('/')
    password = request.POST['pw']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(
        name=request.POST['name'],
        email=request.POST['email'],
        password=pw_hash,
        )
    request.session['userID'] = new_user.id
    return redirect('/success')

def success(request):
    if 'userID' in request.session:
        context = {
            #'logged_in_user' : User.objects.get(id=request.session['userID']).name,
            'logged_in_user' : User.objects.get(id=request.session['userID']),
            'all_quotes': Quote.objects.all(),
            'my_quotes': Quote.objects.filter(favorite = User.objects.get(id=request.session['userID'])),
            'other_quotes': Quote.objects.exclude(favorite = User.objects.get(id=request.session['userID'])),
        }
        return render(request, 'display_quotes.html', context)
    return redirect ('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='login')
            return redirect('/')
    request.session['userID']=User.objects.get(email=request.POST['email']).id
    return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect ('/')
####################################################################################
#   QUOTES          

# IF CREATE IS ON DIFFERENT PAGE
# def add_quote(request):
#     return render(request, 'create_quote.html')

def create_quote(request):
    print(f'posting a quote: {request.POST}')
    quote_errors = Quote.objects.quote_validator(request.POST)
    if len(quote_errors) > 0:
        for key, value in quote_errors.items():
            messages.error(request, value, extra_tags='quote_error')
        return redirect('/success')
    new_quote = Quote.objects.create(
        author=request.POST['author'], 
        quote=request.POST['quote'],
        posted_by=User.objects.get(id=request.session['userID']))
        #many to many skipping
    return redirect ('/success')

def add_to_fav(request, idItem):
    quote_to_fav = Quote.objects.get(id = idItem)
    logged_in_user = User.objects.get(id=request.session['userID'])
    quote_to_fav.favorite.add(logged_in_user)
    return redirect('/success')

def remove_from_fav(request, idItem):
    quote_to_fav = Quote.objects.get(id = idItem)
    logged_in_user = User.objects.get(id=request.session['userID'])
    quote_to_fav.favorite.remove(logged_in_user)
    return redirect ('/success')

def edit_quote(request, idItem):
    editor = Quote.objects.get(id=idItem)
    context = {
        'editor': editor
    }
    return render(request, 'edit_quote.html', context)
    
def update_quote(request, idItem):
    quote_errors = Quote.objects.quote_validator(request.POST)
    if len(quote_errors) > 0:
        for key, value in quote_errors.items():
            messages.error(request, value, extra_tags='quote_error')
        return redirect(f'/edit_quote/{idItem}')
    else:
        print(request.POST)
        updated_quote = Quote.objects.get(id=idItem)
        updated_quote.author =  request.POST['author'] 
        updated_quote.quote = request.POST['quote'] 
        updated_quote.save()
        return redirect ('/success')

def delete_quote(request, idItem):
    selected_quote = Quote.objects.get(id=idItem)
    selected_quote.delete()
    return redirect('/success')


def posted_by(request, idItem):
    if 'userID' in request.session:
        context = {
            'usertoshow' : User.objects.get(id=idItem).name,
            'quotes_created_by_user': Quote.objects.filter(posted_by = User.objects.get(id=idItem)),
        }
        return render(request, 'posted_by.html', context)
    return redirect ('/')

























