
# moloshop/apps/core/templatetags/core_tags.py

from django import template
from django.templatetags.static import static

register = template.Library()


''' Главное (горизонтальное) меню'''
@register.inclusion_tag('core/includes/main_menu.html', takes_context=True)
def core_tags_main_menu(context):
    user = context['request'].user

    menu_items = [
        {'title': "Главная", 'url_name': 'core:home', 'children': []},
        {'title': "О сервисе", 'url_name': 'core:about', 'children': [
            {'title': "Портфолио", 'url_name': 'core:portfolio'},
        ]},
        {'title': "FAG", 'url_name': 'core:fag', 'children': []},
        {'title': "Доска объявлений", 'url_name': 'core:board', 'children': []},
        {'title': "Витрина", 'url_name': 'core:showcase', 'children': []},
      ]
    if user.is_authenticated:
        menu_items.append({'title': "Личный кабинет", 'url_name': 'userpanel:main_profile', 'children': []},)
        menu_items.append({'title': "Выйти", 'url_name': 'users:logout', 'children': [
            {'title': "Выйти (web)", 'url_name': 'users:logout'},
            {'title': "Выйти (api)", 'url_name': 'users_api:logout'},
        ]})
    else:
        menu_items.append({'title': "Войти", 'url_name': 'users:login', 'children': [
            {'title': "Войти (web)", 'url_name': 'users:login'},
            {'title': "Войти (api)", 'url_name': 'users_api:login'},
        ]})
        menu_items.append({'title': "Регистрация", 'url_name': 'users:register', 'children': [
            {'title': "Регистрация (web)", 'url_name': 'users:register'},
            {'title': "Регистрация (api)", 'url_name': 'users_api:register'},
        ]})
    return {'menu_items': menu_items}


# ''' Быстрая навигация '''
# @register.inclusion_tag('core/includes/fast_nav_block.html')
# def fast_nav():
#     return {}