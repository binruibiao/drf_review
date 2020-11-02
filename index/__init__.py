# index的__init__.py文件
from django.apps import AppConfig
import os
# 修改App在Admin后台显示的名称
default_app_config = 'index.IndexConfig'

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class IndexConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '师生信息表'