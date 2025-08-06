
# D:\PythonProject\cu_moloshop\moloshop\apps\core\apps.py

from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
    verbose_name = 'Общая утилита, миксин, базовая модель'
    verbose_name_plural = 'Общие утилиты, миксины, базовые модели'
