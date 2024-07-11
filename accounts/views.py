from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


# Registration View
class UserRegistrationView(FormView):
    template_name = "accounts/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        print(form.cleaned_data.get("image"))
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


# login
class UserLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self) -> str:
        return reverse_lazy("homepage")


# logout
def UserLogoutView(request):
    logout(request)
    return redirect("homepage")


# profile
def profile(request):
    return render(request, "accounts/profile.html")
