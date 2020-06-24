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
    print(f'plz dont hack: {pw_hash}')
    newUser = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=pw_hash,
        )
    request.session['userID'] = newUser.id
    return redirect('/success')

def success(request):
    if 'userID' in request.session:
        context = {
            'name' : User.objects.get(id=request.session['userID']).first_name,
        }
        return render(request, 'login.html', context)
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
