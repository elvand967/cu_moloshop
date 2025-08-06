# apps/users/urls_api.py

from django.urls import path
from .views_api import RegisterAPIView, LoginAPIView, LogoutAPIView

app_name = "users_api"

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
]
