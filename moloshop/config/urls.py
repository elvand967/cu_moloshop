
# moloshop/config/urls.py


from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключаем core.urls для доступа к /admin/named-urls-json/
    path('admin-api/', include('apps.core.urls')),
    path('', include('apps.core.urls')),
    path('userpanel/', include('apps.userpanel.urls', namespace='userpanel')),
    path('users/', include('apps.users.urls_web', namespace='users')),
    path('api/users/', include('apps.users.urls_api', namespace='users_api')),
    path('accounts/', include('allauth.urls')),  # Это подключит все маршруты allauth, включая соцсети
    path('ckeditor/', include('ckeditor_uploader.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
