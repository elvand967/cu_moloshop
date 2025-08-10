
# moloshop/apps/userpanel/models/profile.py

import os
import hashlib
from io import BytesIO
from PIL import Image
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.files.base import ContentFile
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField


def user_avatar_upload_path(instance, filename):
    """
    Путь и имя файла аватарки на основе хэша email.
    """
    email = instance.user.email.lower().strip()
    ext = filename.split('.')[-1]
    hashed_email = hashlib.md5(email.encode()).hexdigest()
    filename = f"{hashed_email}.{ext}"
    return os.path.join("avatars", f"user_{instance.user.id}", filename)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name=_("Пользователь")
    )

    avatar = models.ImageField(
        upload_to=user_avatar_upload_path,
        blank=True,
        null=True,
        verbose_name=_("Аватар")
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')],
        verbose_name=_("Телефон")
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name=_("Дата рождения")
    )

    bio = RichTextField(
        blank=True,
        verbose_name=_("О себе")
    )

    website = models.URLField(
        blank=True,
        verbose_name=_("Веб-сайт")
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Создан"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Обновлен"))

    class Meta:
        verbose_name = _("Профиль пользователя")
        verbose_name_plural = _("Профили пользователей")

    def __str__(self):
        return f"Профиль {self.user.get_full_name() or self.user.email}"

    def save(self, *args, **kwargs):
        # Удаляем старую аватарку, если загружается новая
        try:
            old_avatar = UserProfile.objects.get(pk=self.pk).avatar
            if old_avatar and old_avatar != self.avatar:
                old_avatar.delete(save=False)
        except UserProfile.DoesNotExist:
            pass

        # Обработка аватарки
        if self.avatar:
            img = Image.open(self.avatar)
            max_size = (400, 400)
            img.thumbnail(max_size, Image.LANCZOS)

            buffer = BytesIO()
            img_format = img.format or 'JPEG'
            img.save(buffer, format=img_format, quality=85)
            buffer.seek(0)

            self.avatar = ContentFile(buffer.read(), self.avatar.name)

        super().save(*args, **kwargs)
