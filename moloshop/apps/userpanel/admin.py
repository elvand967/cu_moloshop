# moloshop/apps/userpanel/admin.py

from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models.menu import ProfileMenuCategory
from .forms import ProfileMenuCategoryForm
from .models.profile import UserProfile
from ckeditor.widgets import CKEditorWidget
from django import forms


@admin.register(ProfileMenuCategory)
class ProfileMenuAdmin(DraggableMPTTAdmin):
    form = ProfileMenuCategoryForm

    list_display = (
        'tree_actions',
        'indented_title',
        'slug',
        'url',
        'order',
        'is_named_url'
    )
    list_editable = ('order',)
    search_fields = ('name', 'slug', 'url')


class UserProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = UserProfile
        fields = '__all__'


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileForm
    list_display = ("user", "phone_number", "date_of_birth", "created_at")
    search_fields = ("user__email", "phone_number")
    readonly_fields = ("created_at", "updated_at")
