from django.contrib.auth.models import User
from .constants import USER_RATING
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    publication_date = models.DateField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(upload_to="book_images/", blank=True, null=True)
    borrowing_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(choices=USER_RATING)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.user.user.username} review on - {self.book.title}"
