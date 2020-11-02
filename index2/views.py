from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView, status
from index2.models import *
from rest_framework import mixins, generics, viewsets
from index2.serializers import *


class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        student_id = kwargs.get('id')
        if student_id:
            try:
                student = User.objects.get(pk=student_id)
            except Exception as e:
                print(e.__traceback__.tb_frame.f_back)
                return Response({
                    'status': 400,
                    'message': 'BadRequest'
                })
            else:
                return Response({
                    'status': 200,
                    'message': '查询单个用户成功',
                    'results': UserSerializer(student).data
                })
        students = User.objects.all()
        return Response({
            'status': 200,
            'message': '查询全体用户成功',
            'results': UserSerializer(students, many=True).data
        })

    def post(self, request, *args, **kwargs):
        post_data = request.data
        if not isinstance(post_data, dict) or post_data == {}:
            return Response({
                'status': 400,
                'message': 'BadRequest'
            })
        deser_res = UserDeSerializer(data=post_data)
        if deser_res.is_valid():
            student = deser_res.save()
            return Response({
                'status': 200,
                'message': '新增单个用户成功',
                'results': UserSerializer(student).data
            })
        else:
            return Response({
                'status': 400,
                'message': 'BadRequest',
                'results': deser_res.errors
            })

class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"

    def user_login(self, request, *args, **kwargs):
        post_data = request.data
        if isinstance(post_data, dict) and post_data.get('user_name') and \
            post_data.get('password'):
            for item in self.get_queryset():
                if post_data.get('user_name') == item.user_name and \
                        post_data.get('password') == item.password:
                    return Response({
                        'status': status.HTTP_200_OK,
                        'message': '登录成功',
                        'errno': 0
                    })
            else:
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': '登录失败',
                    'errno': -1
                })
        else:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': '登录失败',
                'errno': -1
            })

    def user_register(self, request, *args, **kwargs):
        put_data = request.data
        if isinstance(put_data, dict) and put_data.get('user_name') and \
            put_data.get('password') and put_data.get('email'):
            for item in self.get_queryset():
                if put_data.get('user_name') == item.user_name:
                    return Response({
                        'status': status.HTTP_400_BAD_REQUEST,
                        'message': '该用户已注册',
                        'errno': -1
                    })
            else:
                return Response({
                    'status': status.HTTP_200_OK,
                    'message': '注册成功',
                    'errno': 0
                })
        else:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': '注册失败',
                'errno': -1
            })

    def get_user_list(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
