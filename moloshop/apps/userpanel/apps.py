
# moloshop/apps/userpanel/apps.py

from django.apps import AppConfig

class UserpanelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.userpanel'
    verbose_name = "Панель пользователя"

    def ready(self):
        import apps.userpanel.signals
