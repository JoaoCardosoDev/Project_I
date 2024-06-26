from django import forms
from django.contrib.auth.models import User
from .models import NormalUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

# class NormalUserForm(forms.ModelForm):
#     class Meta:
#         model = NormalUser
#         fields = ('email', 'max_quota')

from django.contrib.auth.forms import UserCreationForm

class NormalUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = NormalUser
        fields = ('username', 'password1', 'password2', 'email')