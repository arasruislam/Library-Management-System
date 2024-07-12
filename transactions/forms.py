from .models import Transaction
from django import forms


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["amount", "transaction_type"]

    def __init__(self, *args, **kwargs):
        self.user_account = kwargs.pop("account") 
        super().__init__(*args, **kwargs)
        self.fields["transaction_type"].disabled = True 
        self.fields["transaction_type"].widget = (
            forms.HiddenInput()
        )  # user er theke hide kora thakbe

    def save(self, commit=True):
        self.instance.account = self.user_account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()
