from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    
    path('book/<int:id>', views.book),
    path('addBook', views.addBook),
    path('submitBook', views.submitBook),
    path('bookAddAuthor', views.bookAddAuthor),

    path('author/<int:id>', views.author),
    path('addAuthor', views.addAuthor),
    path('submitAuthor', views.submitAuthor),
    path('authorAddBook', views.authorAddBook),
    
]
