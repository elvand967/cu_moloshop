
# moloshop/apps/core/views.py

from django.shortcuts import render


def home(request):
    data = {
        'title': 'Домашняя страница',
        'info': 'Первые шаги настройки',
    }
    return render(request, 'core/home.html', context=data)


def about(request):
    data = {
        'title': 'О сервисе',
        'info': 'О сервисе',
    }
    return render(request, 'core/about.html', context=data)


def fag(request):
    data = {
        'title': 'FAG',
        'info': 'Часто задаваемые вопросы',
    }
    return render(request, 'core/fag.html', context=data)


def board(request):
    data = {
        'title': 'Доска объявлений',
        'info': 'Страница доски объявлений',
    }
    return render(request, 'core/board.html', context=data)


def showcase(request):
    data = {
        'title': 'Витрина',
        'info': 'Витрина товаров и услуг исполнителей',
    }
    return render(request, 'core/showcase.html', context=data)


def feedback(request):
    data = {
        'title': 'Обратная связь',  # тестируем отработку 'title' по умолчанию в шаблоне
        'info': 'Здесь должна быть форма обратной связи',
    }
    return render(request, 'core/feedback.html', context=data)


def portfolio(request):
    data = {
        'title': 'Портфолио',
        'info': 'Портфолио: новые презентации и разработки',
    }
    return render(request, 'core/portfolio.html', context=data)


# --moloshop/apps/core/views.py--
from django.http import JsonResponse
from .utils import get_named_url_info

def named_urls_api(request):
    """
    API: /core/api/named-urls/
    Возвращает JSON со всеми именованными маршрутами.
    """
    return JsonResponse(get_named_url_info(), safe=False)


