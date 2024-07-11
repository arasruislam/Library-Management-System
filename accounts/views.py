from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm
from django.shortcuts import redirect
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


def UserLogoutView(request):
    logout(request)
    return redirect("homepage")
