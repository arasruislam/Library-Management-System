from django import forms
from .models import Book
from accounts.models import BorrowingHistory, UserLibraryAccount

# class BorrowBookForm(forms.ModelForm):
class BorrowForm(forms.ModelForm):
    model: BorrowingHistory
    fields = ['book']

    def __init__(self, *args, **kwargs):
        self.user_account = kwargs.pop('account')
        super().__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.all()

    def clean_book(self):
        book = self.cleaned_data.get('book')

        if book.borrowing_price > self.user_account.balance:
            raise forms.ValidationError(
                f"Insufficient balance to borrow this book. You need {book.borrowing_price} tk but have {self.user_account.balance} tk"
            )
        return book
    
    def save(self, commit = True):
        self.instance.balance = self.user_account
        return super().save(commit)
