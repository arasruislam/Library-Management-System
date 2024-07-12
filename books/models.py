from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    publication_date = models.DateField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(upload_to="book_images/", blank=True, null=True)
    borrowing_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.title
