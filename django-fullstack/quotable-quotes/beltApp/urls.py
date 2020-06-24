from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),

    path("create_quote", views.create_quote),
    path('edit_quote/<idItem>', views.edit_quote), 
    path('update_quote/<idItem>', views.update_quote), 
    path('delete_quote/<idItem>', views.delete_quote), 

    path("add_to_fav/<idItem>", views.add_to_fav),
    path("remove_from_fav/<idItem>", views.remove_from_fav),

    path('posted_by/<idItem>', views.posted_by), 
]

# IF CREATE IS ON DIFFERENT PAGE
    #path("add_quote", views.add_quote),
