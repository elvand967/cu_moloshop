# moloshop/apps/userpanel/admin.py

from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models.menu import ProfileMenuCategory
from .forms import ProfileMenuCategoryForm


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

