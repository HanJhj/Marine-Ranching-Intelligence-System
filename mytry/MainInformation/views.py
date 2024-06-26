from django.shortcuts import render
import pandas as pd
from .models import Water

# Create your views here.


def MainInformation(request):
    try:
        # 获取今天的数据
        today = pd.Timestamp.now().strftime('%Y-%m-%d')
        water = Water.objects.get(time__startswith=today)
    except Water.DoesNotExist:
        water = Water.objects.get(time__startswith='2024-06-22')
    
    all_water = Water.objects.all().order_by('-time')
    water_num = all_water.count()
    if not all_water:
        all_water = None
    context = {'today_water': water,
               'all_water': all_water,
               'water_num': water_num}
    return render(request, 'MainInformation/MainInformation.html', context)

def MainInformation_user(request):
    try:
        # 获取今天的数据
        today = pd.Timestamp.now().strftime('%Y-%m-%d')
        water = Water.objects.get(time__startswith=today)
    except Water.DoesNotExist:
        water = Water.objects.get(time__startswith='2024-06-22')
    
    all_water = Water.objects.all().order_by('-time')
    water_num = all_water.count()
    if not all_water:
        all_water = None
    context = {'today_water': water,
               'all_water': all_water,
               'water_num': water_num}
    return render(request, 'MainInformation/MainInformation_user.html', context)

def insert_water_data(time, water_type, temperature, ph, dissolved_oxygen, conductivity, 
                      turbidity, permanganate_index, ammonia_nitrogen, total_phosphorus, total_nitrogen):
    Water.objects.create(time=time, type=water_type, temperature=temperature, 
                         ph=ph, dissolved_oxygen=dissolved_oxygen, conductivity=conductivity, 
                         turbidity=turbidity, permanganate_index=permanganate_index, 
                         ammonia_nitrogen=ammonia_nitrogen, total_phosphorus=total_phosphorus, 
                         total_nitrogen=total_nitrogen)
    

def clear_water_data():
    # 删除Water表中的所有记录
    Water.objects.all().delete()
    print("水质数据表已清空。")
def Upload(request):
    if request.method == 'POST'and len(request.FILES) > 0:
        f = request.FILES['file']
        excel_type = f.name.split('.')[1]
        if excel_type in ['xlsx', 'xls']:
            clear_water_data()
            data = pd.read_excel(f,
                                 date_format=lambda x: pd.to_datetime(x, format="%Y/%m/%d")
)
            times = pd.to_datetime(data.iloc[:,0]).dt.date
            for i in range(len(data)):
                # time = data.iloc[i,0]
                time = times.iloc[i]
                water_type = data.iloc[i,1]
                temperature = data.iloc[i,2]
                ph = data.iloc[i,3]
                dissolved_oxygen = data.iloc[i,4]
                conductivity = data.iloc[i,5]
                turbidity = data.iloc[i,6]
                permanganate_index = data.iloc[i,7]
                ammonia_nitrogen = data.iloc[i,8]
                total_phosphorus = data.iloc[i,9]
                total_nitrogen = data.iloc[i,10]
                insert_water_data(time, water_type, temperature, ph, dissolved_oxygen, conductivity, 
                                  turbidity, permanganate_index, ammonia_nitrogen, total_phosphorus, total_nitrogen)
        else:
            error = '上传文件类型错误！'
            print(error)
        print('上传成功！')
            
    return render(request, 'MainInformation/MainInformation.html')

