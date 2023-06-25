
from .forms import EditBookForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Purchase, Borrowing

def home(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books/home.html', context)

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {'book': book}
    return render(request, 'books/book-detail.html', context)


def add_book(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image-file')
        book = Book.objects.create(
            title=data['title'],
            author=data['author'],
            isbn=data['isbn'],
            price=data['price'],
            image=image
        )
        return redirect('books:home')
    return render(request, 'books/add-book.html')

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = EditBookForm(instance=book)

    if request.method == 'POST':
        form = EditBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:home')

    context = {'form': form}
    return render(request, 'books/update-book.html', context)

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('books:home')

    context = {'book': book}
    return render(request, 'books/delete-book.html', context)

def purchase_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if book.is_available and book.available_quantity > 0:
        book.available_quantity -= 1
        if book.available_quantity == 0:
            book.is_available = False
        book.save()

        purchase = Purchase(book=book, purchaser=request.user)
        purchase.save()

        return redirect('books:book-detail', id=book.id)
    else:
        return render(request, 'book_not_available.html')

def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if book.is_available and book.available_quantity > 0:
        book.is_available = False
        book.save()

        borrowing = Borrowing(book=book, borrower=request.user)
        borrowing.save()

        return redirect('books:book-detail', id=book.id)
    else:
        return render(request, 'book_not_available.html')


