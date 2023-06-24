
from .forms import EditBookForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.shortcuts import render, redirect


def home(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request,'books/home.html', context)

def book_detail(request, id):
    book = Book.objects.get(pk=id)
    context = {'book': book}
    return render(request, 'books/book-detail.html', context)

def add_book(request):
    
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image-file')
        book = Book.objects.create(
           title = data['title'],
           author = data['author'],
           isbn = data['isbn'],
           price = data['price'],
           image = image
        )
        
        return redirect('home')
    return render(request, 'books/add-book.html')


def edit_book(request, id):

    book = Book.objects.get(pk=id)
    form = EditBookForm(instance=book)
    if request.method == 'POST':
        form = EditBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    context = {'form': form}
    return render(request, 'books/update-book.html', context)

def delete_book(request, id):
    
    book = Book.objects.get(pk=id)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    context = {'book': book}
    return render(request, 'books/delete-book.html', context)
