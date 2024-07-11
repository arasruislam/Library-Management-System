from .views import UserRegistrationView, UserLogoutView, UserLoginView
from django.urls import path

urlpatterns = [
    path("signup/", UserRegistrationView.as_view(), name="registration"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView, name="logout"),
]
