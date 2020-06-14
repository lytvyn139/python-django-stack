
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
""" 
SELECT * FROM onetomanyApp_author;

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell
from onetomanyApp.models import *

    # access to query Author and Book, they will return empty query sets
Author.objects.all()    # <QuerySet []>
Book.objects.all()      # <QuerySet []>

    # creating new instance of author, and print his name
new_author = Author.objects.create(name = "Fyodor Emelianenko")
new_author.name          

    # create a book, and author is a foreign key that pointing to another instance
new_book = Book.objects.create(title = "Crime and Punishment", author = new_author)
new_book.title          # Crime and Punishment     
new_book.author.name    # Fyodor Emelianenko

    # create another book
another_book = Book.objects.create(title = "The Brothers Karamazov", author = new_author)
another_book.title          # The Brothers Karamazov
another_book.author.name    # Fyodor Emelianenko

    # all of the books, that our new_author has written
new_author.books        # <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x7fed858e3e50>
new_author.books.all()  # <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]>

    # query all the books that new_author has written
Book.objects.get(id=1).title # Crime and Punishment
Book.objects.get(id=2).title # The Brothers Karamazov

Book.objects.get(id=1).author # <Author: Author object (1)>
Book.objects.get(id=1).author.books
#<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x7fed859fd310>


    # LOOPING
for book in new_author.books.all():
<tab>print(book.title)
<enter>
<enter>
Crime and Punishment
The Brothers Karamazov

"""

