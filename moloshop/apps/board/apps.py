
# D:\PythonProject\cu_moloshop\moloshop\apps\board\apps.py

from django.apps import AppConfig


class BoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.board'
    verbose_name = 'Доска бъявлений'
    verbose_name_plural = 'Доски бъявлений'
