from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("logout", views.logout),
    path('registerUser', views.register),
    path("showUser", views.show)
]

