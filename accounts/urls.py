from .views import UserRegistrationView, UserLogoutView
from django.urls import path

urlpatterns = [
    path("signup/", UserRegistrationView.as_view(), name="registration"),
    path("logout/", UserLogoutView, name="logout"),
]
