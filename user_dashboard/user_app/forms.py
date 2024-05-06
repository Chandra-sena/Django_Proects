# user_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'profile_picture', 'username', 'email', 'password1', 'password2', 'address_line1', 'city', 'state', 'pincode', 'user_type']
