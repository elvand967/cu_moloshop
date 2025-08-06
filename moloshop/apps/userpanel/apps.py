from django.apps import AppConfig


class UserpanelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.userpanel'  # ← это правильно!
    verbose_name = 'Кабинет пользователя'
    verbose_name_plural = 'Кабинеты пользователей'