
# moloshop/apps/core/utils.py

from pytils.translit import slugify as pytils_slugify

def generate_unique_slug(model_class, name, slug_field='slug', scope=None):
    """
    Генерирует уникальный slug для модели.

    Пояснение параметров:
    - model_class: класс модели, для которой генерируем slug (например, BusinessProduct)
    - name: исходное имя (строка), из которого будет сделан slug
    - slug_field: имя поля модели, где хранится slug (обычно 'slug')
    - scope: словарь с условиями, которые ограничивают область проверки уникальности,
      т.е. уникальность будет проверяться только в объектах, удовлетворяющих этому условию.
      Например, {'business': business} — уникальность в рамках одного бизнеса.

    Логика работы:
    1. Создаём базовый slug из имени с помощью pytils_slugify (к примеру, 'Продукт №1' -> 'produkt-1').
    2. Проверяем, есть ли уже объект с таким slug в базе, при этом применяем условия из scope, если он есть.
    3. Если slug занят, добавляем суффикс с числом, например 'produkt-1-1', 'produkt-1-2' и так далее,
       пока не найдём уникальный slug.
    4. Возвращаем уникальный slug.
    """
    base_slug = pytils_slugify(name)
    slug = base_slug
    counter = 1

    if scope is None:
        scope = {}

    # Проверяем, существует ли уже такой slug с учетом scope (условий)
    while model_class.objects.filter(**{**scope, slug_field: slug}).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1

    return slug


# moloshop/apps/core/utils.py
from django.urls import get_resolver, URLPattern, URLResolver

def list_all_url_names():
    """
    Рекурсивно получает все URL имена из всех url-конфигураций,
    включая все пространства имён.
    Возвращает отсортированный и уникальный список кортежей (name, name).
    """
    resolver = get_resolver()
    url_names = set()

    def recurse_patterns(patterns, namespace_prefix=''):
        for pattern in patterns:
            if isinstance(pattern, URLPattern):
                full_name = f"{namespace_prefix}:{pattern.name}" if namespace_prefix and pattern.name else pattern.name
                if full_name:
                    url_names.add(full_name)
            elif isinstance(pattern, URLResolver):
                ns = f"{namespace_prefix}:{pattern.namespace}" if namespace_prefix and pattern.namespace else pattern.namespace or ''
                recurse_patterns(pattern.url_patterns, ns)

    recurse_patterns(resolver.url_patterns)
    sorted_names = sorted(url_names)
    return [(name, name) for name in sorted_names]


# ---moloshop/apps/core/utils.py---
from django.urls import get_resolver
from django.utils.text import slugify
import re

def get_named_url_info():
    """
    Возвращает список словарей с info по именованным URL:
    - full_name: 'userpanel:test1'
    - name: 'test1'
    - app_name: 'userpanel'
    - pattern: строка пути (пример: 'test1/')
    - params: словарь параметров с пустыми значениями, например {'slug': ''}
    """
    allowed_namespaces = {'userpanel', 'users', 'core', 'landing'}

    url_info_list = []

    def walk_patterns(patterns, prefix='', app_name=None):
        for pattern in patterns:
            if hasattr(pattern, 'url_patterns'):
                ns = pattern.namespace
                new_app_name = ns if ns else app_name
                new_prefix = f"{prefix}{ns}:" if ns else prefix
                if ns is None or ns in allowed_namespaces:
                    walk_patterns(pattern.url_patterns, new_prefix, new_app_name)
            elif pattern.name:
                full_name = f"{prefix}{pattern.name}"
                # Пытаемся получить pattern.regex или pattern.pattern
                pattern_str = ''
                try:
                    # Django 2.0+
                    pattern_str = getattr(pattern.pattern, '_route', '')  # строка маршрута
                except AttributeError:
                    pattern_str = ''

                # Ищем параметры в пути, например <slug:slug>
                param_names = re.findall(r'<(?:\w+:)?(\w+)>', pattern_str)
                params = {name: '' for name in param_names}

                url_info_list.append({
                    'full_name': full_name,
                    'name': pattern.name,
                    'app_name': app_name or '',
                    'pattern': pattern_str,
                    'params': params,
                })

    resolver = get_resolver()
    walk_patterns(resolver.url_patterns)

    return url_info_list

