from .views import UserRegistrationView
from django.urls import path

urlpatterns = [
    path("signup/", UserRegistrationView.as_view(), name="registration"),
]
