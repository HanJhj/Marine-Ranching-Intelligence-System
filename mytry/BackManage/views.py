from django.shortcuts import render

# Create your views here.


def BackManage(request):
    context = {'title1': 'My Page Title1'}  # 数据字典
    # return render(request, '/templates/trend.html', context)  # 使用模板
    return render(request, 'BackManage/chronic.html', context)