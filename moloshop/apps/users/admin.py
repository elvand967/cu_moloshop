
# D:\PythonProject\cu_moloshop\moloshop\apps\users\admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = (
        'email', 'nickname', 'full_name', 'auth_provider_choice',
        'phone_number', 'is_staff', 'is_active'
    )
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'auth_provider_choice')
    ordering = ('email',)
    search_fields = ('email', 'nickname', 'full_name', 'phone_number')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Личные данные', {'fields': ('nickname', 'full_name', 'auth_provider_choice', 'phone_number')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'nickname', 'full_name', 'auth_provider_choice',
                'phone_number', 'password1', 'password2',
                'is_active', 'is_staff', 'is_superuser'
            ),
        }),
    )

admin.site.register(User, UserAdmin)


