from django.contrib import admin
from .models import Currency, ServicePolicy

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    search_fields = ['code', 'name']


@admin.register(ServicePolicy)
class ServicePolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'updated_at')  # отображаемые поля в списке
    search_fields = ('title', 'slug')                # поля для поиска
    prepopulated_fields = {'slug': ('title',)}       # автоматическое заполнение slug из title
    readonly_fields = ('updated_at',)                 # поля только для чтения
