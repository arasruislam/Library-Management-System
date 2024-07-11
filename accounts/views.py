from django.views.generic.edit import FormView
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy


# Registration View
class UserRegistrationView(FormView):
    template_name = "accounts/user_registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)