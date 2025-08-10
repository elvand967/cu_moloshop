
# moloshop/apps/userpanel/views/main.py

from django.shortcuts import render

def main_profile(request):
    data = {
        'title': 'Личный кабинет пользователя',
        'info': 'Форма ввода/редактирования персональных данных',
        "current_path": request.path,
    }
    return render(request, 'userpanel/main_profile.html', context=data)

def my_ads(request):
    data = {
        'title': 'Мои объявления',
        'info': 'Моя история объявлений',
        "current_path": request.path,
    }
    return render(request, 'userpanel/my_ads.html', context=data)

def my_orders(request):
    data = {
        'title': 'Мои заказы',
        'info': 'Список моих заказов',
        "current_path": request.path,
    }
    return render(request, 'userpanel/my_orders.html', context=data)

def purchase_history(request):
    data = {
        'title': 'История покупок',
        'info': 'Моя история покупок',
        "current_path": request.path,
    }
    return render(request, 'userpanel/purchase_history.html', context=data)


def test1(request):
    data = {
        'title': 'test1',
        'info': 'Мой тест №-1',
        "current_path": request.path,
    }
    return render(request, 'userpanel/test1.html', context=data)

def test2(request):
    data = {
        'title': 'test2',
        'info': 'Мой тест №-2',
        "current_path": request.path,
    }
    return render(request, 'userpanel/test2.html', context=data)

def test3(request):
    data = {
        'title': 'test3',
        'info': 'Мой тест №-3',
        "current_path": request.path,
    }
    return render(request, 'userpanel/test3.html', context=data)

def test4(request):
    data = {
        'title': 'test4',
        'info': 'Мой тест №-4',
        "current_path": request.path,
    }
    return render(request, 'userpanel/test4.html', context=data)