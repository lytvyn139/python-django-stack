from django.shortcuts import render, redirect
from .models import User, Item
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    #print request.post to seee if the server can collect all the form info
    print(request.POST)
    #validate the info from form
    validationErrors = User.objects.regValidator(request.POST)
    print('printing validationErrors below')
    print(validationErrors)
    #if the form info is NOT filled out properly, redirect them back to the page where the form is and show them validation errors
    if len(validationErrors) > 0:
        for key, value in validationErrors.items():
            messages.error(request, value )
        return redirect("/")
    #else!!!!! if form info IS filled out properly, create a user using the form info 
    else:
        #encrypt the password the user wants to register with first
        safePw = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
        print("PRINTING HASHED PASSSWORD BELOW!!!")
        print(safePw)
        #theennnnn create the user using that encrypted password
        newuser = User.objects.create(name = request.POST['form_name'], email = request.POST['form_email'], password = safePw)
    #log the user in and take them to the success page by storing their id in session
        request.session['loggedinId'] = newuser.id
    #redirect to the route that the form needs to 
        return redirect("/success")

def login(request):
    print(request.POST)
    validationErrors = User.objects.loginvalidator(request.POST)
    if len(validationErrors) > 0:
        for key, value in validationErrors.items():
            messages.error(request, value )
        return redirect("/")
    else:
        loggedUser = User.objects.filter(email = request.POST['form_email'])
        print(loggedUser)
        #put their id in session
        request.session['loggedinId'] = loggedUser[0].id
        return redirect('/success')


def home(request):
    if 'loggedinId' not in request.session:
        return redirect('/')
    context = {
        'loggedinUser': User.objects.get(id= request.session['loggedinId']),
        'allitems': Item.objects.all(),
        'favitems': Item.objects.filter(favoritors = User.objects.get(id= request.session['loggedinId'])),
        'nonfavitems': Item.objects.exclude(favoritors = User.objects.get(id= request.session['loggedinId']))
    }
    return render(request, 'main.html', context)


def showCreateItemPage(request):
    return render(request, 'newitem.html')

def createItem(request):
    print(request.POST)
    #validate the info from form to make sure that it is filld out properly
    newitem = Item.objects.create(name = request.POST['itemName'], uploader = User.objects.get(id= request.session['loggedinId']))
    return redirect("/success")

def favoriteItem(request, idItem):
    #get the item obj
    itemToFav = Item.objects.get(id = idItem)
    #get the user obj
    loggedinuser = User.objects.get(id= request.session['loggedinId'])
    #make the many to may join
    itemToFav.favoritors.add(loggedinuser)
    #redirect
    return redirect('/success')


def logout(request):
    request.session.clear()
    # del request.session['loggedinId']
    return redirect("/")
