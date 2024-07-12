from django.db import models
from accounts.models import UserLibraryAccount
from .constants import TRANSACTION_TYPE, DEPOSIT


# Create your models here.

class Transaction(models.Model):
    account = models.ForeignKey(
        UserLibraryAccount, related_name="transactions", on_delete=models.CASCADE
    )

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance_after_transaction = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null=True, default=DEPOSIT)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False)

    class Meta:
        ordering = ["timestamp"]

    def save(self, *args, **kwargs):
        self.transaction_type = DEPOSIT  
        super().save(*args, **kwargs)
