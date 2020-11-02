from django.db import models

# Create your models here.
from django.utils.html import format_html


class Student(models.Model):
    gender_choices = (
        (0, 'male'),
        (1, 'female')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, null=True, blank=True)
    age = models.SmallIntegerField(null=True, blank=True)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    school = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = 't_student'
        verbose_name = '学生表'
        verbose_name_plural = '学生表'

    def __str__(self):
        return self.name

class Teacher(models.Model):
    gender_choices = (
        (0, 'male'),
        (1, 'female')
    )
    position_choices = (
        (0, '辅导员'),
        (1, '讲师'),
        (2, '副教授'),
        (3, '教授'),
        (4, '院长'),
        (5, '书记')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, null=True, blank=True)
    age = models.SmallIntegerField(null=True, blank=True)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    school = models.CharField(max_length=30, null=True, blank=True)
    position = models.SmallIntegerField(choices=position_choices, default=1)

    class Meta:
        db_table = 't_teacher'
        verbose_name = '教师表'
        verbose_name_plural = '教师表'

    def __str__(self):
        return self.name

    def colored_name(self):
        if 'Ben' == self.name:
            color_code = '#e1005a'
        else:
            color_code = '#42b983'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.name
        )

    colored_name.short_description = 'name'
