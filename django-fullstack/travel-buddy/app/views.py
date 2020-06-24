from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

####################################################################################
# LOGIN 

def index(request):
    if 'userid' in request.session:
        return redirect('/travels/')
    return render(request, 'index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        password = request.POST['pwd']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(name=request.POST['name'],username=request.POST['username'],password=pw_hash)
        messages.success(request, "Your account is created, please login !")
        return redirect("/")

def login(request):
    user = User.objects.filter(username=request.POST['username'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['pwd'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/travels')
    messages.error(request,'invalid username/password')
    return redirect("/")

def logout(request):
    if 'userid' in request.session:
        del request.session['userid']
    return redirect('/')

####################################################################################
# TRAVEL 

def addTravel(request):
    if 'userid' not in request.session:
        return redirect('/')
    return render(request, "add_travel.html")

def addTripPlan(request):
    errors = TravelPlan.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect("/travels/add")
    else:
        this_plan = TravelPlan.objects.create(
            destination=request.POST['destination'],
            description=request.POST['description'],
            dateFrom=request.POST['date_from'],
            dateTo=request.POST['date_to'], 
            creator=User.objects.get(id=request.session['userid']))
        this_trip = Trip.objects.create(plan=this_plan)
        this_trip.users.add(User.objects.get(id=request.session['userid']))
        return redirect('/travels')

def travels(request):
    if 'userid' not in request.session:
        return redirect('/')
    userTripIds = []
    for each_trip in Trip.objects.filter(users = User.objects.get(id=request.session['userid'])):
        userTripIds.append(each_trip.id)
    context = {
        "this_user" : User.objects.get(id=request.session['userid']),
        "user_trips" : Trip.objects.filter(users = User.objects.get(id=request.session['userid'])),
        "other_travelPlans" : TravelPlan.objects.exclude(creator_id=request.session['userid']),
        "user_trip_ids" : userTripIds
    }
    return render(request, 'travels.html', context)

def destination(request, planid):
    if 'userid' not in request.session:
        return redirect('/')
    this_plan = TravelPlan.objects.get(id=planid)
    trips = this_plan.trips.all()
    for trip in trips:
        users = trip.users.all()
    context = {
        'plan' : TravelPlan.objects.get(id=planid),
        'users' : users
    }
    return render(request, "destination.html", context)

def joinTrip(request, planid):
    if 'userid' not in request.session:
        return redirect('/')
    Trip.objects.get(plan=planid).users.add(User.objects.get(id=request.session['userid']))
    return redirect('/')

