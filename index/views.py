from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets
from index.models import *
from index.serializers import *

class StudentAPIView(APIView):
    def get(self, request, *args, **kwargs):
        student_id = kwargs.get('id')
        if student_id:
            try:
                student = Student.objects.get(pk=student_id)
            except Exception as e:
                print(e.__traceback__.tb_frame.f_back)
                return Response({
                    'status': 400,
                    'message': 'BadRequest'
                })
            else:
                return Response({
                    'status': 200,
                    'message': '查询单个学生成功',
                    'results': StudentSerializer(student).data
                })
        students = Student.objects.all()
        return Response({
            'status': 200,
            'message': '查询全体学生成功',
            'results': StudentSerializer(students, many=True).data
        })

    def post(self, request, *args, **kwargs):
        post_data = request.data
        if not isinstance(post_data, dict) or post_data == {}:
            return Response({
                'status': 400,
                'message': 'BadRequest'
            })
        deser_res = StudentDeSerializer(data=post_data)
        if deser_res.is_valid():
            student = deser_res.save()
            return Response({
                'status': 200,
                'message': '新增单个学生成功',
                'results': StudentSerializer(student).data
            })
        else:
            return Response({
                'status': 400,
                'message': 'BadRequest',
                'results': deser_res.errors
            })

class TeacherAPIView(APIView):
    def get(self, request, *args, **kwargs):
        teacher_id = kwargs.get('id')
        if teacher_id:
            try:
                teacher = Teacher.objects.get(pk=teacher_id)
            except Exception as e:
                print(e.__traceback__.tb_frame.f_back)
                return Response({
                    'status': 400,
                    'message': 'BadRequest'
                })
            else:
                return Response({
                    'status': 200,
                    'message': '查询单个教师成功',
                    'results': TeacherSerializer(teacher).data
                })
        teachers = Teacher.objects.all()
        return Response({
            'status': 200,
            'message': '查询全体教师成功',
            'results': TeacherSerializer(teachers, many=True).data
        })

    def post(self, request, *args, **kwargs):
        post_data = request.data
        if not isinstance(post_data, dict) or post_data == {}:
            return Response({
                'status': 400,
                'message': 'BadRequest'
            })
        deser_res = TeacherDeSerializer(data=post_data)
        if deser_res.is_valid():
            teacher = deser_res.save()
            return Response({
                'status': 200,
                'message': '新增单个教师成功',
                'results': TeacherSerializer(teacher).data
            })
        else:
            return Response({
                'status': 400,
                'message': 'BadRequest',
                'results': deser_res.errors
            })




