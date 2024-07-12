from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404
from .models import Book, Category


# Create your views here.


# Book details
class BookDetailsView(TemplateView):
    template_name = "book_details.html"

    def get_context_data(self, **kwargs):
        book_id = self.kwargs["id"]
        book = get_object_or_404(Book, pk=book_id)
        context = super().get_context_data(**kwargs)
        context["book"] = book
        return context


# Category View
class CategoryView(ListView):
    template_name = "category.html"
    context_object_name = "books"

    def get_queryset(self):
        category_slug = self.kwargs["category_slug"]
        category = get_object_or_404(Category, slug=category_slug)
        return Book.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs["category_slug"]
        context["categories"] = Category.objects.all()
        context["selected_category"] = get_object_or_404(Category, slug=category_slug)
        context["is_homepage"] = False
        context["total_result"] = self.get_queryset().count()
        return context
