#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/10/31 12:33
#@Author: 卞瑞彪
#@File  : urls.py
from django.urls import path
from index import views
urlpatterns = [
    path('student/', views.StudentAPIView.as_view()),
    path('student/<int:id>/', views.StudentAPIView.as_view()),
    path('teacher/', views.TeacherAPIView.as_view()),
    path('teacher/<int:id>/', views.TeacherAPIView.as_view()),
]