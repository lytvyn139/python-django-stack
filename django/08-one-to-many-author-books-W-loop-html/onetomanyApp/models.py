
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
""" 
SELECT * FROM onetomanyApp_author;

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell
from onetomanyApp.models import *

Author.objects.all()    # <QuerySet []>
Book.objects.all()      # <QuerySet []>

new_author = Author.objects.create(name = "Iurii Lytvyn")
new_author = Author.objects.create(name = "Volodya Dosta")
new_author.name         # Volodya Dosta

new_book = Book.objects.create(title = "Crime and Punishment", author = new_author)
new_book = Book.objects.create(title = "Test4", author = new_author)
new_book.title          # Crime and Punishment     
new_book.author.name    # Volodya Dosta

other_book = Book.objects.create(title = "The Brothers Karamazov", author = new_author)
other_book.title        # The Brothers Karamazov
new_book.author.name    # Volodya Dosta

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

