from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from accounts.models import UserLibraryAccount

# Create your models here.

class Borrowing_Details(models.Model):
    user = models.ForeignKey(UserLibraryAccount,on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.user.username} borrowed this {self.book.title}"
    

class Deposit(models.Model):
    user = models.ForeignKey(UserLibraryAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} deposited successfully {self.amount}$"