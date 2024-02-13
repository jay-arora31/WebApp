from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")
        labels = {
            "username": "",
            "email": "",
            "password1": "",
            "password2": "",
        }
        placeholders = {
            "username": "Username",
            "email": "Email Address",
            "password1": "Create Password",
            "password2": "Confirm Password",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["placeholder"] = self.Meta.placeholders.get(field, "")
