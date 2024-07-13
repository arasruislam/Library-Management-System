from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404
from .models import Book, Category
from django.views.generic import CreateView
from django.views import View
from accounts.models import BorrowingHistory, UserLibraryAccount
from .forms import BorrowForm
from django.urls import reverse_lazy
from django.contrib import messages

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


# Borrow Book View
# class BorrowBookView(LoginRequiredMixin, CreateView):
#     model = BorrowingHistory
#     form_class = BorrowForm
#     template_name = "borrow_form.html"
#     success_url = reverse_lazy("profile")

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs.update({"account": self.request.user.account})
#         return kwargs

#     def form_valid(self, form):
#         book = form.cleaned_data.get("book")
#         account = self.request.user.account

#         if book.borrowing_price > account.balance:
#             messages.error(self.request, "Insufficient balance to borrow this book.")

#             return self.form_invalid(form)

#         account.balance -= book.borrowing_price
#         account.save(update_fields=["balance"])

#         messages.success(
#             self.request,
#             f"You have successfully borrowed {book.title} for {book.borrowing_price} tk.",
#         )
#         return super().form_valid(form)


class BorrowBookView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        book_id = kwargs.get("id")
        book = get_object_or_404(Book, pk=book_id)
        account = request.user.account

        already_borrowed = BorrowingHistory.objects.filter(
            user=account, book=book, returned_at__isnull=True
        ).exists()
        if already_borrowed:
            messages.error(
                request,
                "You have already borrowed this book. To borrow it again, please return it first.",
            )
            return redirect("homepage")

        if book.borrowing_price > account.balance:
            messages.error(self.request, "Insufficient balance to borrow this book.")
            return redirect("homepage")

        account.balance -= book.borrowing_price
        account.save(update_fields=["balance"])

        BorrowingHistory.objects.create(user=account, book=book)
        messages.success(
            request,
            f"You have successfully borrowed {book.title} for {book.borrowing_price} tk.",
        )
        return redirect("profile")
