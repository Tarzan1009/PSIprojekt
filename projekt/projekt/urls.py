"""projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.urls import re_path
from szkody import views
from szkody.views import *
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls')),

    path('SamochodList/', SamochodList.as_view()),
    path('SamochodDetails/', SamochodDetail.as_view()),

    path('CustomUserList/', CustomUserList.as_view()),
    path('CustomUserDetails/', CustomUserDetail.as_view()),

    path('KlientList/', KlientList.as_view()),
    path('KlientDetails/', KlientDetail.as_view()),

    path('KlientList/', KlientList.as_view()),
    path('KlientDetails/', KlientDetail.as_view()),

    path('ZdarzenieList/', ZdarzenieList.as_view()),
    path('ZdarzenieDetails/', ZdarzenieDetail.as_view()),

    path('UczestnicyList/', UczestnicyList.as_view()),
    path('UczestnicyDetails/', UczestnicyDetail.as_view()),

    path('UserList/', CustomUserList.as_view()),
    path('UserDetails/', CustomUserDetail.as_view()),
]
