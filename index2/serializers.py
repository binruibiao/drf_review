#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/10/31 14:37
#@Author: 卞瑞彪
#@File  : serializers.py
from django.core import exceptions
from rest_framework import serializers
from index2.models import *
class UserSerializer(serializers.ModelSerializer):
    '''
    用户类的序列化器
    '''
    # user_name = serializers.CharField(allow_null=True, allow_blank=True)
    # password = serializers.CharField(allow_null=True, allow_blank=True)
    # email = serializers.EmailField(allow_null=True, allow_blank=True)
    class Meta:
        model = User
        fields = ('user_name', 'password', 'email', 'beauty')
        # fields = '__all__'

        depth = 1

'''
ModelSerializer内部自己实现了create()方法去保存对象，不再需要程序员手动编写create()方法
(1) extra_kwargs: 可以通过此参数为反序列化器添加校验规则
(2) 全局钩子和局部钩子同样可以自定义校验规则（仍可以正常使用）
(3) fields中指定的字段必须提供值（不可为空）
'''
class UserDeSerializer(serializers.ModelSerializer):
    # user_name = serializers.CharField(
    #     max_length=4,
    #     min_length=2,
    #     error_messages={
    #         'max_length': '名字过长',
    #         'min_length': '名字过短'
    #     },
    #     allow_null=False,
    #     allow_blank=False
    # )
    # password = serializers.CharField(allow_null=False, allow_blank=False)
    # email = serializers.EmailField(allow_null=False, allow_blank=False)

    class Meta:
        model = User
        fields = ('user_name', 'password', 'email')
        extra_kwargs = {
            'user_name': {
                'required': True,
                'min_length': 2,
                'max_length': 4,
                'error_messages': {
                    'required': '用户名不可为空',
                    'min_length': '名字过短',
                    'max_length': '名字过长'
                }
            },
            'password': {
                'required': True,
                'min_length': 6,
                'max_length': 16,
                'error_messages': {
                    'required': '密码不能为空',
                    'min_length': '密码过短',
                    'max_length': '密码过长'
                }
            }
        }

    # def validate(self, attrs):
    #     password = attrs.get('password')
    #     if len(password) < 6 or len(password) > 16:
    #         raise exceptions.ValidationError('密码不合法')
    #     return attrs
    # 继承Serializer需要自实现create方法，用于新增用户
    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)

'''
补充：
序列化嵌套使用能够实现多表查询（意思是：在一个序列化器的定义中实例化另一个序列化器）

class PressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Press
        fields = ('press_name', 'address', 'range')

class BookSerializer(serializers.ModelSerializer):
    
    publish = PressSerializer()
    
    class Meta:
        model = Book
        fields = ('book_name', 'price', 'publish')
    
'''