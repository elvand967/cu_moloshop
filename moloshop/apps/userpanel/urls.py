
# moloshop/apps/userpanel/urls.py

from django.urls import path
from .views import *
from .views_service import policy_list, policy_detail

app_name = "userpanel" # пространство имён

urlpatterns = [
    path('', main_profile, name='main_profile'),
    path('my-ads/', my_ads, name='my_ads'),  # мои объявления
    path('my-orders/', my_orders, name='my_orders'),   # мои заказы
    path('purchase-history/', purchase_history, name='purchase_history'),   # история покупок
    path('test1/', test1, name='test1'),   # мои тесты
    path('test2/', test2, name='test2'),  # мои тесты
    path('test3/', test3, name='test3'),
    path('test4/', test4, name='test4'),
    path('policies/', policy_list, name='policy_list'),
    path('policies/<slug:slug>/', policy_detail, name='policy_detail'),
]
