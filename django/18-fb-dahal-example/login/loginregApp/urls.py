from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path("success", views.home),
    path("login", views.login),
    path("wishItems/create", views.showCreateItemPage),
    path("createItem", views.createItem),
    path("favoriteItem/<idItem>", views.favoriteItem),
    path("logout", views.logout)
]
