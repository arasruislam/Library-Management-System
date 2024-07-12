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
        )

    def save(self, commit=True):
        self.instance.account = self.user_account
        self.instance.balance_after_transaction = self.user_account.balance
        return super().save()


class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.cleaned_data.get("amount")
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f"You need to deposit at least {min_deposit_amount} $"
            )

        return amount
