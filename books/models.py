from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isbn = models.CharField(max_length=100)
    
    image = models.ImageField(null=False, blank=False, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    available_quantity = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']


class Purchase(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchaser = models.ForeignKey(User, on_delete=models.CASCADE)
   


class Borrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
   
