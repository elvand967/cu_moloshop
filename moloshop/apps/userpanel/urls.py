
# moloshop/apps/userpanel/urls.py

from django.urls import path
from .views.main import (
    main_profile,
    my_ads,
    my_orders,
    purchase_history,
    test1,
    test2,
    test3,
    test4,
)

from apps.userpanel.views.views_service import policy_list, policy_detail
from .views.avatar import generate_avatar_view

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

    path('avatar/default/<int:user_id>/', generate_avatar_view, name='default-avatar'),
]
