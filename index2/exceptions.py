#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/10/31 14:37
#@Author: 卞瑞彪
#@File  : exceptions.py

from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import status

def my_exception_handler(exc, context):
    error = '%s %s %s' % (context["view"], context["request"].method, exc)
    print(error)

    response = exception_handler(exc, context)
    if response is None:
        return Response(
            {
                'message': '上帝请稍等,程序猿正在加紧处理中~',
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    return response
