from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum
from .models import Transaction
from .forms import DepositForm
from .constants import DEPOSIT
from django.views import View
from datetime import datetime


class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = "transactions/transaction_form.html"
    model = Transaction
    title = ""
    success_url = reverse_lazy("profile")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"account": self.request.user.account})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"title": self.title})
        return context


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = "Deposit"

    def get_initial(self):
        # initial = super().get_initial()
        initial = {"transaction_type": DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get("amount")
        account = self.request.user.account
        account.balance += amount
        account.save(update_fields=["balance"])

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully',
        )
        return super().form_valid(form)
