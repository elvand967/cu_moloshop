
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
