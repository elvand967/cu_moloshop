
# moloshop/apps/users/models.py

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone

from apps.core.models import UUIDModel


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class AuthProvider(models.IntegerChoices):
    UNKNOWN = 0, 'unknown'
    EMAIL = 1, 'email'
    PHONE = 2, 'phone'
    GOOGLE = 3, 'google'
    APPLE = 4, 'apple'

class User(UUIDModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=150, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    auth_provider_choice = models.IntegerField(
        choices=AuthProvider.choices,
        default=AuthProvider.EMAIL
    )
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # можно добавить другие обязательные поля

    '''
    Методы get_full_name() и get_short_name() — это стандартные методы AbstractUser и AbstractBaseUser, 
    используемые в Django (например, в админке, при логах, в шаблонах и т.п.).
    Так как реализована кастомная модель на основе AbstractBaseUser, 
    необходимо реализовать эти методы вручную, если цель, чтобы admin и другие части Django работали корректно.
    '''
    def get_full_name(self):
        return self.full_name or self.email  # или любое другое предпочтительное поведение

    def get_short_name(self):
        return self.full_name.split()[0] if self.full_name else self.email

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
