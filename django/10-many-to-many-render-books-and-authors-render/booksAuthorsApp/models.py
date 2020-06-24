from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    authors = models.ManyToManyField(Author, related_name="bookz")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

""" 
python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py shell
from booksAuthorsApp.models import Book, Author

    #BOOK1
Book.objects.create(title="C# in Depth", desc="Fourth Edition is your key to unlocking the powerful new features added to the language in C# 5, 6, and 7. Following the expert guidance of C# legend Jon Skeet, you'll master asynchronous functions, expression-bodied members, interpolated strings, tuples, and much more.")
    #BOOK2
Book.objects.create(title="Java Programming (5th Edition)", desc="This is the 5th edition of Murach's classic Java book that's trained thousands of developers in the last 15 years. Now fully updated to Java 9, this book helps any programmer learn Java faster and better than ever before: It's the one Java book that presents object-oriented features like inheritance, interfaces, and polymorphism in a way that's both understandable and useful in the real world.")
    #BOOK3
Book.objects.create(title="Ruby on Rails", desc="Ruby on Rails™ Tutorial by Michael Hartl has become a must-read for developers learning how to build Rails apps Peter Cooper, Editor of Ruby Inside")
    #BOOK4
Book.objects.create(title="Eloquent JavaScript", desc="JavaScript lies at the heart of almost every modern web application, from social apps like Twitter to browser-based, complex language that you can use to build full-scale applications")

    #Author for book 1
Author.objects.create(first_name="John", last_name="Sket")
    #Authors for book 2
Author.objects.create(first_name="Joel", last_name="Murah")
Author.objects.create(first_name="Anne", last_name="Boehm")
Author.objects.create(first_name="Mary", last_name="Delamater")

    #Author for book 3
Author.objects.create(first_name="Michael", last_name="Harlh")
    #Author4
Author.objects.create(first_name="Marijn", last_name="Haverbeke")

    # VARS
book1 = Book.objects.get(id = 1)
book2 = Book.objects.get(id = 2)
book3 = Book.objects.get(id = 3)
book4 = Book.objects.get(id = 4)
author1 = Author.objects.get(id = 1)
author2 = Author.objects.get(id = 2)
author3 = Author.objects.get(id = 3)
author4 = Author.objects.get(id = 4)
author5 = Author.objects.get(id = 5)
author6 = Author.objects.get(id = 6)

author1.bookz.add(book1)    #Assign author1 to book1

author2.bookz.add(book2)    #Assign author2-3-4 to book2
author3.bookz.add(book2)
author4.bookz.add(book2)
    
author5.bookz.add(book3)    #Assign author5 to book3

author6.bookz.add(book4)    #Assign author6 to book4
"""