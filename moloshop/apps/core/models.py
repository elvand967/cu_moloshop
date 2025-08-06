
# moloshop/apps/core/models.py

import uuid
from django.db import models
from ckeditor.fields import RichTextField   # форматироваание текста
# from ckeditor_uploader.fields import RichTextUploadingField    # форматироваание текста с поддержкой изображений

'''
Реализация UUID в качестве id для моделей.

Django корректно работает с UUIDField как с основным ключом.
В PostgreSQL такие поля будут иметь natvie тип uuid,
в других СУБД — обычно тип CHAR(32) или CHAR(36).

Во всех новых моделях вместо наследования от models.Model
используйте наследование от UUIDModel.

ПРИМЕР:
    from core.models import UUIDModel

    class Product(UUIDModel):
        name = models.CharField(max_length=100)
        # остальные поля

Поле 'id' будет автоматически создано в новой модели с типом UUIDField и ключом primary_key=True.
'''
class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Currency(UUIDModel):
    """
    Глобальный справочник валют для всего проекта.
    """
    code = models.CharField(max_length=3, unique=True, help_text="ISO 4217 код, например: BYN, USD, EUR")
    name = models.CharField(max_length=50, help_text="Название валюты на русском", blank=True)
    symbol = models.CharField(max_length=8, help_text="Символ: ₽, $, € и т.д.", blank=True)

    def __str__(self):
        return f"{self.code} ({self.symbol})" if self.symbol else self.code


class ServicePolicy(UUIDModel):
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="Уникальный идентификатор для пути")
    seo_title = models.CharField(
        max_length=70,
        blank=True,
        verbose_name='SEO заголовок'
    )
    seo_description = models.CharField(
        max_length=160,
        blank=True,
        verbose_name='SEO описание'
    )
    content = models.TextField(verbose_name="Содержание")
    description = RichTextField()   # форматируемый текст
    # description = RichTextUploadingField()  # форматируемый текст с поддержкой изображений
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")

    class Meta:
        verbose_name = "Служебная информация"
        verbose_name_plural = "Служебная информация"

    def __str__(self):
        return self.title