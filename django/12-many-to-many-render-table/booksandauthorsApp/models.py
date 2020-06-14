from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    authors = models.ManyToManyField(Book, related_name="author_books")
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
""" 
#SELECT * FROM booksandauthorsApp_book;

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell
from booksandauthorsApp.models import Book, Author

Book.objects.create(title="C Sharp", desc="C# book")
Book.objects.create(title="Java", desc="good ole java book")
Book.objects.create(title="Python", desc="cobra style book")
Book.objects.create(title="PHP", desc="PHP not dead !")
Book.objects.create(title="Ruby", desc="pure gem")
Author.objects.create(first_name="Jane", last_name="Austen")
Author.objects.create(first_name="Emily", last_name="Dickinson")
Author.objects.create(first_name="Fyodor", last_name="Dostoevsky")
Author.objects.create(first_name="William", last_name="Shakespeare")
Author.objects.create(first_name="Lau", last_name="Tzu")

exit()
adding to Author class: notes = models.TextField(null=True)

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell
from booksandauthorsApp.models import Book, Author

temp = Book.objects.get(id = 1)
temp.title = "C#"
temp.save()

temp = Author.objects.get(id = 4)
temp.title = "Bill"
temp.save()

    #VARS
first_author = Author.objects.get(id = 1)
second_author = Author.objects.get(id = 2)
third_author = Author.objects.get(id = 3)
fourth_author = Author.objects.get(id = 4)
fifth_author = Author.objects.get(id = 5)
book1 = Book.objects.get(id = 1)
book2 = Book.objects.get(id = 2)
book3 = Book.objects.get(id = 3)
book4 = Book.objects.get(id = 4)
book5 = Book.objects.get(id = 5)

    #Assign the first author to the first 2 books
first_author.authors.add(book1)
first_author.authors.add(book2)

    #Assign second author to the first 3 books
second_author.authors.add(book1)
second_author.authors.add(book2)
second_author.authors.add(book3)

    #Assign the third author to the first 4 books
third_author.authors.add(book1)
third_author.authors.add(book2)
third_author.authors.add(book3)
third_author.authors.add(book4)

    #Assign the fourth author to the first 5 books (or in other words, all the books)
fourth_author.authors.add(book1)
fourth_author.authors.add(book2)
fourth_author.authors.add(book3)
fourth_author.authors.add(book4)
fourth_author.authors.add(book5)

    #Retrieve all the authors for the 3rd book
book3.author_books.all()

    #Remove the first author of the 3rd book
first_author.authors.remove(book1)

    #Add the 5th author as one of the authors of the 2nd book
fifth_author.authors.add(book2)

    #Find all the books that the 3rd author is part of 
third_author.authors.all()

    #Find all the authors that contributed to the 5th book
book5.author_books.all()

"""
