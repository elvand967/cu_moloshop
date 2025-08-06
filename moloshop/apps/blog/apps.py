
# D:\PythonProject\cu_moloshop\moloshop\apps\blog\apps.py

from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.blog'
    verbose_name = 'Блог'
    verbose_name_plural = 'Блоги'