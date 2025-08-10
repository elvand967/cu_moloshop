
# moloshop/apps/userpanel/signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from .models.profile import UserProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Создание или обновление профиля пользователя при сохранении User.
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()


@receiver(post_delete, sender=UserProfile)
def delete_user_avatar(sender, instance, **kwargs):
    """
    Удаление файла аватарки при удалении профиля.
    """
    if instance.avatar:
        instance.avatar.delete(save=False)
