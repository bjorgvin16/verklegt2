from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm): #inherits the normal django user creation form but is costomized within this class
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'email', 'password1', 'password2']