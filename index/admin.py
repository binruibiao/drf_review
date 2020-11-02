from django.contrib import admin
from index.models import *
# Register your models here.

admin.site.site_title = '师生信息管理系统'
admin.site.site_header = '师生信息管理系统'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # 在新增页面、修改页面设置布局
    fieldsets = (
        ('不可折叠信息', {
            'fields': ('name', 'age', 'gender')
        }),
        ('可折叠信息', {
            'classes': ('collapse', ),
            'fields': ('school', ),
        })
    )
    # 设置可排序字段
    sortable_by = ['id', 'name', 'age']
    # 在数据列表页面设置显示的字段
    list_display = ['id', 'name', 'age', 'gender', 'school']
    # 在数据列表页面设置跳转字段（即跳转而不编辑）
    list_display_links = ['name', 'age', 'gender']
    # 在数据列表页面设置可编辑字段（即可编辑而不跳转）
    list_editable = []
    # 在数据列表页面指定每页显示数
    list_per_page = 100
    # 在数据列表页面指定每页显示最大数
    list_max_show_all = 200
    # 在数据列表页面设置过滤器
    list_filter = ['name', 'age', 'gender']
    # 在数据列表页面设置可搜索字段
    search_fields = ['id', 'name', 'age', 'gender', 'school']
    # 在修改页面新增“另存为”功能
    save_as = True
    # 设置动作栏的位置
    actions_on_bottom = True
    actions_on_top = False

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # 在新增页面、修改页面设置布局
    fieldsets = (
        ('不可可折叠信息', {
            'fields': ('name', 'age', 'gender')
        }),
        ('可折叠信息', {
            'classes': ('collapse', ),
            'fields': ('school', 'position'),
        })
    )
    #
    list_max_show_all = 200
    list_per_page = 100
    list_display = ['id', 'colored_name', 'age', 'gender', 'school', 'position']
    list_editable = ['position']
    list_display_links = ['colored_name', 'age', 'gender']
    list_filter = ['name', 'age', 'gender', 'position']
    search_fields = ['id', 'name', 'age', 'gender', 'school', 'position']
    save_as = True
    actions_on_top = False
    actions_on_bottom = True
