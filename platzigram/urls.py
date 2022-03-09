"""Modulo de urls django"""
# Django
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(('posts.urls', 'posts'), namespace='posts')),

    path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
