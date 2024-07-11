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
                image=image,
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


class UserLibraryAccountUpdateForm(forms.ModelForm):
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
            "first_name",
            "last_name",
            "email",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": (
                        "appearance-none block w-full bg-gray-200 "
                        "text-gray-700 border border-gray-200 rounded "
                        "py-3 px-4 leading-tight focus:outline-none "
                        "focus:bg-white focus:border-gray-500"
                    )
                }
            )

        if self.instance:
            try:
                user_account = self.instance.account
                # user_address = self.instance.address
            except UserLibraryAccount.DoesNotExist:
                user_account = None
                # user_address = None

            if user_account:
                self.fields["gender"].initial = user_account.gender
                self.fields["birth_date"].initial = user_account.birth_date
                self.fields["street_address"].initial = user_account.street_address
                self.fields["city"].initial = user_account.city
                self.fields["postal_code"].initial = user_account.postal_code
                self.fields["country"].initial = user_account.country
                self.fields["image"].initial = user_account.image

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            user_account, created = UserLibraryAccount.objects.get_or_create(user=user)

            user_account.gender = self.cleaned_data["gender"]
            user_account.birth_date = self.cleaned_data["birth_date"]
            user_account.street_address = self.cleaned_data["street_address"]
            user_account.city = self.cleaned_data["city"]
            user_account.postal_code = self.cleaned_data["postal_code"]
            user_account.country = self.cleaned_data["country"]
            if self.cleaned_data["image"]:
                user_account.image = self.cleaned_data["image"]
            user_account.save()

        return user
