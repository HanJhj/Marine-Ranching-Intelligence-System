
from django.shortcuts import render
from .models import HardwareInfo
from datetime import date
from django.apps import apps
# Create your views here.

def DataCenter(request):
    # 设备信息
    latest_info = HardwareInfo.objects.filter(date=date.today()).first()
    # 数据库表统计信息
    all_apps = apps.get_app_configs()# 获取所有已安装的 app
    table_info_list = [] # 遍历所有 app 来获取模型
    for app_config in all_apps:
        # 获取 app 下的所有模型
        models = app_config.get_models()
        for model in models:
            # 获取模型的元数据，如表名等
            table_name = model._meta.db_table
            verbose_name = model._meta.verbose_name_plural
            table_info_list.append({
                'app_label': app_config.label,
                'table_name': table_name,
                'verbose_name': verbose_name,
            })
    
    # 按照 app_label 排序，可选
    table_info_list.sort(key=lambda x: x['app_label'])
    context = {
        'latest_info': latest_info,
        'table_info_list': table_info_list,
    }
    return render(request, 'DataCenter/NCDindex.html', context)




