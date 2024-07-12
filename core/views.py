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

