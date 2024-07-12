from django.urls import path
from .views import BookDetailsView, demo

urlpatterns = [
    path(
        "books/book/<int:id>/book_details/",
        BookDetailsView.as_view(),
        name="book_details",
    ),

]
