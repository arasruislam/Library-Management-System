from .views import (
    BookDetailsView,
    CategoryView,
    BorrowBookView,
    ReturnBookView,
    BookReviewView,
)
from django.urls import path

urlpatterns = [
    path(
        "books/book/<int:id>/book_details/",
        BookDetailsView.as_view(),
        name="book_details",
    ),
    path("book/review/<int:id>/", BookReviewView.as_view(), name="review_book"),
    path(
        "categories/<slug:category_slug>/",
        CategoryView.as_view(),
        name="category_books",
    ),
    path("book/<int:id>/borrow/", BorrowBookView.as_view(), name="borrow_book"),
    path(
        "borrow_history/<int:id>/return/",
        ReturnBookView.as_view(),
        name="return_book",
    ),
]
