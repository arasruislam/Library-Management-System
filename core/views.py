from django.views.generic import TemplateView
from books.models import Book
from django.shortcuts import get_object_or_404, render


# Create your views here.
class HomeView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.all()
        return context


def demo(request):
    return render(request, "book_details.html")


# Book details
class BookDetailsView(TemplateView):
    template_name = "book_details.html"

    def get_context_data(self, **kwargs):
        book_id = self.kwargs["id"]
        book = get_object_or_404(Book, pk=book_id)
        context = super().get_context_data(**kwargs)
        context["book"] = book
        return context
