"""usersapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from allauth.account.views import ConfirmEmailView
from rest_framework import routers
from panel.views import GeeksViewSet, GeeksViewSet2, GeeksViewSet3, GeeksViewSet4, GeeksViewSet5, GeeksViewSet6

router = routers.DefaultRouter()
router.register(r'a1', GeeksViewSet)
router.register(r'a2', GeeksViewSet2)
router.register(r'a3', GeeksViewSet3)
router.register(r'a4', GeeksViewSet4)
router.register(r'a5', GeeksViewSet5)
router.register(r'a6', GeeksViewSet6)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    re_path('rest-auth/registration/account-confirm-email/(?P<key>.+)/',ConfirmEmailView.as_view(),         name='account_confirm_email'),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),

    path('levels/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))


]
