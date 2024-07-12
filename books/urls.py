from django.urls import path
from .views import BookDetailsView, CategoryView

urlpatterns = [
    path(
        "books/book/<int:id>/book_details/",
        BookDetailsView.as_view(),
        name="book_details",
    ),
    path(
        "categories/<slug:category_slug>/", CategoryView.as_view(), name="category_books"
    ),
]
