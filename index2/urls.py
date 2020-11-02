#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/10/31 14:37
#@Author: 卞瑞彪
#@File  : urls.py

from django.urls import path
from index2 import views
urlpatterns = [
    path('user/', views.UserAPIView.as_view()),
    path('user/<int:id>/', views.UserAPIView.as_view()),
    path('userviewsets/', views.UserViewSet.as_view({
        'post': 'user_login',
        'put': 'user_register',
        'get': 'get_user_list'
    })),
    path('userviewsets/<int:id>/', views.UserViewSet.as_view({
        'post': 'user_login',
        'put': 'user_register',
        'get': 'get_user_list'
    }))
]