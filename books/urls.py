from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:pk>/', views.book_detail, name='book-detail'),
    path('add-book/', views.add_book, name='add-book'),
    path('edit-book/<int:pk>/', views.edit_book, name='edit-book'),
    path('delete-book/<int:pk>/', views.delete_book, name='delete-book'),
    path('books/<int:book_id>/purchase/', views.purchase_book, name='purchase-book'),
    path('books/<int:book_id>/borrow/', views.borrow_book, name='borrow-book'),
]









