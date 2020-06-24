from django.shortcuts import render, redirect
from . models import Book, Author

def index(request):
    return render(request, 'index.html')

def book(request, id):
    request.session['bookID'] = id
    context = {
        'book': Book.objects.get(id=id),
        'authors': Author.objects.exclude(bookz=id),
    }
    return render(request, 'book.html', context)

def addBook(request):
    context = {
        'bookz': Book.objects.all()
    }
    return render(request, 'add_book.html', context)

def submitBook(request):
    if request.method == "POST":
        Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
        return redirect('/addBook')

def bookAddAuthor(request):
    addedAuthor = Author.objects.get(id = request.POST['authors'])
    bookID = request.session['bookID']
    if request.method == "POST":
        Book.objects.get(id=bookID).authors.add(addedAuthor)
        return redirect(f'/book/{bookID}')

########################################
#  AUTHOR block

def author(request, id):
    request.session['authorID'] = id
    context = {
        'author' : Author.objects.get(id=id),
        'bookz' : Book.objects.exclude(authors=id)
    }
    return render(request, 'author.html', context)

def addAuthor(request):
    context = {
        'authors' : Author.objects.all()
    }
    return render(request, 'add_author.html', context)

def submitAuthor(request):
    if request.method == "POST":
        Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
        return redirect('/addAuthor')

def authorAddBook(request):
    addedBook = Book.objects.get(id = request.POST['bookz'])
    authorID = request.session['authorID']
    if request.method == "POST":
        Author.objects.get(id=authorID).bookz.add(addedBook)
        return redirect(f'/author/{authorID}')