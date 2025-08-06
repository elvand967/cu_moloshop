
# D:\PythonProject\cu_moloshop\moloshop\apps\users\forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', max_length=254)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'nickname', 'full_name', 'auth_provider_choice', 'phone_number')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            'email', 'nickname', 'full_name', 'auth_provider_choice',
            'phone_number', 'is_active', 'is_staff', 'is_superuser'
        )
