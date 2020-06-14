
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<blogId>', views.show),
    path('<blogId>/edit', views.edit),
    path('<blogId>/detele', views.destroy)
]
