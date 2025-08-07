
# moloshop/apps/core/admin.py

from django.contrib import admin
from .models import Currency, ServicePolicy
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ServicePolicyAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(config_name='default'))

    class Meta:
        model = ServicePolicy
        fields = '__all__'

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    search_fields = ['code', 'name']


@admin.register(ServicePolicy)
class ServicePolicyAdmin(admin.ModelAdmin):
    form = ServicePolicyAdminForm
    list_display = ('title', 'slug', 'updated_at')  # отображаемые поля в списке
    search_fields = ('title', 'slug')                # поля для поиска
    prepopulated_fields = {'slug': ('title',)}       # автоматическое заполнение slug из title
    readonly_fields = ('updated_at',)                 # поля только для чтения
