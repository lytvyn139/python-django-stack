from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),

    path('travels/', views.travels),
    path('travels/add/', views.addTravel),
    path('travels/add/addPlan/', views.addTripPlan),
    path('travels/destination/<int:planid>/', views.destination),
    path('travels/joinTrip/<int:planid>/', views.joinTrip),
    
]