from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import WebsiteUser


class DateInput(forms.DateInput):
    input_type = "date"


class RegistrationForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=DateInput)

    class Meta:
        model = WebsiteUser
        fields = [
            "username",
            "email",
            "date_of_birth",
            "number",
            "cat_colour",
            "favourite_movie",
            "profile_photo",
        ]


class ProfileEditForm(UserChangeForm):
    date_of_birth = forms.DateField(required=False)
    number = forms.CharField(max_length=20, required=False)
    cat_colour = forms.CharField(max_length=50, required=False)
    favourite_movie = forms.CharField(max_length=100, required=False)

    class Meta:
        model = WebsiteUser
        fields = (
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "number",
            "cat_colour",
            "favourite_movie",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = forms.HiddenInput()


class UserEditForm(forms.ModelForm):
    class Meta:
        model = WebsiteUser
        fields = [
            "username",
            "email",
            "date_of_birth",
            "number",
            "cat_colour",
            "favourite_movie",
        ]
