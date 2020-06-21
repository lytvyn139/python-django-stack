from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Load login & registration page
def index(request):
    return render(request, 'index.html')

# Register function that validates registration form data & creates new user record with brypt hashed password. Creates session with user's name & redirects to the wall page (through /success route)
def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='register') # extra tag to distinguish registration message from login message
        return redirect('/')
    password = request.POST['pw']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    print(pw_hash)
    newUser = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=pw_hash,
        )
    request.session['userID'] = newUser.id
    return redirect('/success')

# Login function that validates login form data & logs creates user session, redirects to wall page through /success route.
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

def success(request):
    if 'userID' in request.session:
        context = {
            'name' : User.objects.get(id=request.session['userID']).first_name,
            'messages' : Message.objects.all().order_by('-created_at')
        }
        return render(request, 'wall.html', context)
    return redirect ('/')

def message(request):
    Message.objects.create(message = request.POST['message'], user = User.objects.get(id=request.session['userID']))
    return redirect('/success')

def comment(request):
    print(request.POST['messageID'])
    Comment.objects.create(
        comment = request.POST['comment'], 
        user = User.objects.get(id=request.session['userID']), 
        message = Message.objects.get(id = request.POST['messageID'])
    )
    return redirect('/success')

def deleteMessage(request, messageID):
    messageToDelete = Message.objects.get(id = messageID)
    if messageToDelete.user.id == request.session['userID']:
        messageToDelete.delete()
        return redirect('/success')
    return redirect('/success')

def deleteComment(request, commentID):
    commentToDelete = Comment.objects.get(id = commentID)
    if commentToDelete.user.id == request.session['userID']:
        commentToDelete.delete()
        return redirect('/success')
    return redirect('/success')