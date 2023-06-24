from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isbn = models.CharField(max_length=100)
    
    image = models.ImageField(null=False, blank=False, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        ordering = ['-created_at']

