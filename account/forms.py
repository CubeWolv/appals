# myapp/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    pass

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True, error_messages={'required': 'Please enter your email address'})

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
