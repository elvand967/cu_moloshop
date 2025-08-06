
# D:\PythonProject\cu_moloshop\moloshop\apps\billing\apps.py

from django.apps import AppConfig


class BillingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.billing'
    verbose_name = 'Монетизация, тариф, финансы'
    verbose_name_plural = 'Монетизация, тарифы, финансы'