# moloshop/apps/userpanel/forms.py

import json
from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse
from .models.menu import ProfileMenuCategory
from ..core.utils import get_named_url_info  # универсальная функция, возвращающая список URL

class ProfileMenuCategoryForm(forms.ModelForm):
    url = forms.ChoiceField(
        choices=[],
        required=False,
        label='URL name',
        help_text="Выберите URL-шаблон из подключённых пространств имён"
    )

    slug = forms.CharField(
        required=False,
        label='Slug',
        help_text="Автоматически создаётся из URL-пути, но может быть изменён вручную."
                  "! Внимание ! При необходимости передачи параметров корректируй Slug по экземпляру модели",
        widget=forms.TextInput()
    )

    class Meta:
        model = ProfileMenuCategory
        fields = '__all__'
        widgets = {
            'url_params': forms.Textarea(attrs={
                'rows': 4,
                'style': 'resize: vertical; max-height: 200px;',
                'placeholder': '{"slug": "example"}'
            }),
        }

    class Media:
        js = ('userpanel/js/url_autofill.js',)  # подключаем JS для автозаполнения

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Получаем список именованных URL с подробной инфой
        url_info = get_named_url_info()

        # Формируем choices для поля url (выпадающий список)
        choices = [('', '--- Выберите url_name ---')] + [
            (item["full_name"], item["full_name"]) for item in url_info
        ]
        self.fields['url'].choices = choices

        # Добавляем JSON-данные с полной инфой в атрибут data-named-urls-json у поля 'url'
        # Django Form API не позволяет напрямую добавить data-атрибут, поэтому меняем widget.attrs
        self.fields['url'].widget.attrs['data-named-urls-json'] = json.dumps(url_info, ensure_ascii=False)

    def clean(self):
        cleaned_data = super().clean()
        url = cleaned_data.get("url")
        slug = cleaned_data.get("slug")
        url_params = cleaned_data.get("url_params")
        is_named_url = cleaned_data.get("is_named_url")

        # Если slug не указан, но выбран url — используем url (полное имя) в качестве slug по умолчанию
        if not slug and url:
            cleaned_data['slug'] = url

        # Проверка reverse() для именованного URL
        if is_named_url and url:
            try:
                # url_params в форме JSON, передаём в reverse()
                params = url_params or {}
                if isinstance(params, str):
                    import json as js
                    params = js.loads(params) if params else {}
                reverse(url, kwargs=params)
            except Exception as e:
                raise ValidationError(f"reverse('{url}', kwargs={url_params}) не удался: {e}")

        return cleaned_data
