
# apps/users/urls_web.py

from django.urls import path
from . import views_web

app_name = "users"

urlpatterns = [
    path('login/', views_web.login_view, name='login'),
    path('logout/', views_web.logout_view, name='logout'),
    path('register/', views_web.register_view, name='register'),
    path('profile/', views_web.ProfileView.as_view(), name='profile'),
]
