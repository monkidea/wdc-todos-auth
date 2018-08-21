from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views as authtoken_views
from rest_framework.routers import DefaultRouter

from . import drf_views as views


router = DefaultRouter()

router.register('todo', views.TodoViewSet, base_name='todo')

urlpatterns = [
    path('api-token-generate', authtoken_views.obtain_auth_token)
] + router.urls
