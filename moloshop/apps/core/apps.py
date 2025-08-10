
# moloshop/apps/core/apps.py

from django.apps import AppConfig
from apps.core.utils import get_named_url_info

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
    verbose_name = 'Общая утилита, миксин, базовая модель'
    verbose_name_plural = 'Общие утилиты, миксины, базовые модели'

    def ready(self):
        # Сброс кэша при старте
        get_named_url_info()
