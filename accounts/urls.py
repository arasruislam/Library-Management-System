from .views import UserRegistrationView, UserLogoutView, UserLoginView
from django.views.generic import TemplateView
from django.urls import path

urlpatterns = [
    path("signup/", UserRegistrationView.as_view(), name="registration"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView, name="logout"),
    # path("profile/", profile, name="profile"),
    path("profile/", TemplateView.as_view(template_name="accounts/profile.html"), name="profile"),
]
