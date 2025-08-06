# moloshop/apps/userpanel/forms.py

from django import forms
from django.urls import get_resolver, reverse
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from unidecode import unidecode
from .models.menu import ProfileMenuCategory


def get_named_url_choices():
    """
    Возвращает список именованных URL'ов, отфильтрованных по нужным пространствам имён (namespace).
    """
    allowed_namespaces = {
        'userpanel', 'users', 'users_api', 'core', 'landing',
    }

    def walk_patterns(patterns, prefix=''):
        for pattern in patterns:
            if hasattr(pattern, 'url_patterns'):
                namespace = f"{prefix}{pattern.namespace}:" if pattern.namespace else prefix
                if pattern.namespace is None or pattern.namespace in allowed_namespaces:
                    yield from walk_patterns(pattern.url_patterns, namespace)
            elif pattern.name:
                full_name = f"{prefix}{pattern.name}"
                yield (full_name, full_name)

    return sorted(set(walk_patterns(get_resolver().url_patterns)))


class ProfileMenuCategoryForm(forms.ModelForm):
    slug = forms.CharField(
        required=False,
        label='Slug',
        help_text="Автоматически создаётся из названия, но может быть изменён вручную.",
        widget=forms.TextInput()
    )

    url = forms.ChoiceField(
        choices=[],
        required=False,
        label='URL name',
        help_text="Выберите URL-шаблон из подключённых пространств имён"
    )

    class Meta:
        model = ProfileMenuCategory
        fields = '__all__'
        widgets = {
            'url_params': forms.Textarea(attrs={
                'rows': 4,
                'style': 'resize: vertical; max-height: 200px;',
                'placeholder': "{'slug': 'example'}"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Собираем список URL-шаблонов с namespace
        choices = [('', '--- Выберите url_name ---')] + get_named_url_choices()
        self.fields['url'].choices = choices

        # Добавляем текущий url, если он вручную введён и отсутствует в списке
        if self.instance.url and self.instance.url not in dict(choices):
            self.fields['url'].choices.append((self.instance.url, self.instance.url))

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        slug = cleaned_data.get('slug')

        # Генерируем slug, если он не задан
        if not slug and name:
            generated_slug = slugify(unidecode(name))
            cleaned_data['slug'] = generated_slug
            self.instance.slug = generated_slug

        # Проверка reverse() если установлен is_named_url
        url = cleaned_data.get("url")
        url_params = cleaned_data.get("url_params")
        if cleaned_data.get("is_named_url") and url:
            try:
                reverse(url, kwargs=url_params or {})
            except Exception as e:
                raise ValidationError(f"reverse('{url}', kwargs={url_params}) не удался: {e}")

        return cleaned_data
