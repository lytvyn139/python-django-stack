from django.db import models
""" 
Books can be published by many publishers and publishers can publish many books
Many publishers can have  """

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
class Publisher(models.Model):
	name = models.CharField(max_length=255)
	books = models.ManyToManyField(Book, related_name="publishers")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

""" 
SELECT * FROM manytomanyApp_book;
SELECT * FROM manytomanyApp_publisher;

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell
from manytomanyApp.models import Book, Publisher

!! Before we create relationships we need to create instances first !!

# create books
cracking_the_code = Book.objects.create(title="Cracking the code inverview")
east_of_eden = Book.objects.create(title="East of Eden")

# create publishers
penguin = Publisher.objects.create(name="Penguin Publisher")
harper = Publisher.objects.create(name="Penguin Collins Publisher")

#will list all books
Book.objects.all()

#will list all publishers
Publisher.objects.all()


# if you want to add new book to a publishers 
# penguin published cracking_the_code 
#METHOD: instance.field.add(book-that-was published)
penguin.books.add(cracking_the_code)
penguin.books.add(east_of_eden)

#new instance of a a book object
penguin.books.all() 
#<QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]>

penguin.books.first().title

cracking_the_code.publishers.all()
cracking_the_code.publishers.first().name


"""