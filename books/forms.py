from accounts.models import BorrowingHistory
from .models import Book, Review
from django import forms


# class BorrowBookForm(forms.ModelForm):
class BorrowForm(forms.ModelForm):
    class Meta:
        model = BorrowingHistory
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


class ReviewForm(forms.ModelForm):
    class Meta: 
        model = Review
        fields = ['rating', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": (
                        "appearance-none block w-full bg-gray-100"
                        "text-gray-700 border-t-0 border-l-0 border-r-0 border-b-2 border-gray-200 rounded "
                        "py-3 px-4 leading-tight focus:outline-none "
                        "focus:bg-white focus:border-gray-500"
                    )
                }
            )

