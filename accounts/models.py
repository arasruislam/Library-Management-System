from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE
from books.models import Book


# Create your models here.
class UserLibraryAccount(models.Model):
    user = models.OneToOneField(User, related_name="account", on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    initial_deposit_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profile_images/", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.username} - Account No: {self.account_no}"


class BorrowingHistory(models.Model):
    user = models.ForeignKey(
        UserLibraryAccount, related_name="borrow_history", on_delete=models.CASCADE
    )
    book = models.ForeignKey(Book, related_name="borrow_book", on_delete=models.CASCADE)
    borrow_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)
    can_review = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.returned_at is not None:
            self.can_review = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.user.username} borrowed - {self.book.title}"
