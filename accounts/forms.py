from django.contrib.auth.forms import UserCreationForm
from .models import UserLibraryAccount
from django.contrib.auth.models import User
from .constants import GENDER_TYPE
from django import forms


class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "gender",
            "city",
            "postal_code",
            "street_address",
            "country",
            "image",
        ]

    def save(self, commit=True):
        our_user = super().save(commit=False)

        if commit == True:
            our_user.save()
            gender = self.cleaned_data.get("gender")
            postal_code = self.cleaned_data.get("postal_code")
            country = self.cleaned_data.get("country")
            birth_date = self.cleaned_data.get("birth_date")
            city = self.cleaned_data.get("city")
            street_address = self.cleaned_data.get("street_address")
            image = self.cleaned_data.get("image")

            UserLibraryAccount.objects.create(
                user=our_user,
                gender=gender,
                birth_date=birth_date,
                postal_code=postal_code,
                country=country,
                city=city,
                street_address=street_address,
                image = image,
                account_no=100000 + our_user.id,
            )
            return our_user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": (
                        "appearance-none block w-full bg-gray-100 "
                        "text-gray-700 border-t-0 border-l-0 border-r-0 border-b-2 border-gray-200 rounded "
                        "py-3 px-4 leading-tight focus:outline-none "
                        "focus:bg-white focus:border-gray-500"
                    )
                }
            )
