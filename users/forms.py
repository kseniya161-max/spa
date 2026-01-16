from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import User


class CustomUsersCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email')


