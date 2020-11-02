#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/10/31 12:51
#@Author: 卞瑞彪
#@File  : serializers.py
from django.conf import settings
from django.core import exceptions
from rest_framework import serializers
from index.models import *
class StudentSerializer(serializers.Serializer):
    '''
    学生类的序列化器
    '''
    # id = serializers.SerializerMethodField(allow_null=False)
    id = serializers.IntegerField(allow_null=False)
    name = serializers.CharField(allow_null=True, allow_blank=True)
    age = serializers.IntegerField(allow_null=True)
    # gender = serializers.IntegerField()
    gender = serializers.IntegerField(allow_null=True)
    school = serializers.CharField(allow_null=True, allow_blank=True)

    # def get_id(self, obj):
    #     return 1

    # def get_gender(self, obj):
    #     # gender值是choices类型
    #     return 0

class StudentDeSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=4,
        min_length=2,
        error_messages={
            'max_length': '名字过长',
            'min_length': '名字过短'
        },
        allow_null=False,
        allow_blank=False
    )
    age = serializers.IntegerField(allow_null=False)
    gender = serializers.IntegerField(allow_null=False)
    school = serializers.CharField(allow_null=False, allow_blank=False)
    position = serializers.IntegerField(allow_null=False)
    # 继承Serializer需要自实现create方法，为新增学生做准备
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

class TeacherSerializer(serializers.Serializer):
    '''
    教师类的序列化器
    '''
    id = serializers.IntegerField(allow_null=False)
    name = serializers.CharField(allow_null=True, allow_blank=True)
    age = serializers.IntegerField(allow_null=True)
    gender = serializers.IntegerField(allow_null=False)
    school = serializers.CharField(allow_null=True, allow_blank=True)
    position = serializers.IntegerField(allow_null=False)

    # def get_id(self, obj):
    #     return 1
    #
    # def get_gender(self, obj):
    #     return 0

class TeacherDeSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=4,
        min_length=2,
        error_messages={
            'max_length': '名字过长',
            'min_length': '名字过短'
        },
        allow_null=False,
        allow_blank=False
    )
    age = serializers.IntegerField(allow_null=False)
    gender = serializers.IntegerField(allow_null=False)
    school = serializers.CharField(allow_null=False, allow_blank=False)
    position = serializers.IntegerField(allow_null=False)

    # 全局钩子校验器——校验密码一致性
    def validate(self, attrs):
        name = attrs.get('name')
        school = attrs.get('school')
        if name == school:
            raise exceptions.ValidationError('人名和校名不能一样！')
        return attrs

    # 局部钩子校验器——校验用户名的合法性
    # def validated_name(self, value):
    #     if value == "卞瑞彪":
    #         raise exceptions.ValidationError('用户名有误')
    #     if Teacher.objects.filter(name=value):
    #         raise exceptions.ValidationError('用户名已存在')
    #     return value

    # 继承Serializer需要自实现create方法，为新增教师做准备
    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)


