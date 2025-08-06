
# moloshop/config/settings/base.py

import sys
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
# Загружаем .env
load_dotenv(BASE_DIR / '.env')  # загрузка переменных из .env


'''
Добавляем apps/ в системный путь поиска модулей (sys.path),
Позволяем писать в INSTALLED_APPS и импортировать приложения по коротким именам, например: 'users' вместо 'apps.users'.
'''
sys.path.append(str(BASE_DIR / 'apps'))


# Безопасность
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key')
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 'yes')

ALLOWED_HOSTS = []

# Приложения
INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Allauth core ("ядро" — обязательно!)
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # провайдеры — добавить нужные:
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.yandex',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.github',
    # ... остальные по необходимости
    'django_json_widget',
    # Локальные
    'apps.users.apps.UsersConfig',
    'apps.userpanel.apps.UserpanelConfig',
    'apps.core.apps.CoreConfig',
    'apps.marketplace.apps.MarketplaceConfig',
    'apps.landing.apps.LandingConfig',
    'apps.board.apps.BoardConfig',
    'apps.bookings.apps.BookingsConfig',
    'apps.blog.apps.BlogConfig',
    'apps.portfolio.apps.PortfolioConfig',
    'apps.billing.apps.BillingConfig',
    # API
    'rest_framework',
    'rest_framework.authtoken',
    # CKEditor - форматирование документов
    'ckeditor',
    'ckeditor_uploader',  # поддержка загрузки изображений

]


SITE_ID = 1


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',   # <--- добавьте этот слой
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Общие шаблоны
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# База данных (в dev и prod отдельная настройка)
DATABASES = {}


AUTH_USER_MODEL = 'apps.users.User'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Для корректной работы debug_toolbar, email и т.д.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Пароли
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Локализация
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Minsk'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Статика и медиа
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'assets']
STATIC_ROOT = BASE_DIR / 'static_root'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# форматирование с загрузкой изображения (WYSIWYG-редактор)
CKEDITOR_UPLOAD_PATH = 'uploads/'

# (необязательно, для настройки toolbar)
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 'auto',
    },
}


# Авторизация
AUTH_USER_MODEL = 'users.User'  # если кастомная модель

# Логирование (пример)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {'class': 'logging.StreamHandler',},
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
