from django.shortcuts import render
import requests
# Create your views here.


def SmartCenter(request):
    api_key = '006d982064c569b6a16def3a5f704fdc'
    city_name = 'Tianjin'  # 默认城市为北京，但可以根据请求参数改变
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=zh_cn'

    response = requests.get(url)
    context = {}
    if response.status_code == 200:
        weather_data = response.json()
        context = {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed'],
        }
    else:
        context = {'error_message': '无法获取天气信息'}

    return render(request, 'SmartCenter/trend.html', context)

# from datetime import datetime

# def SmartCenter(request):
#     api_key = '006d982064c569b6a16def3a5f704fdc'  # 确保这个API Key支持One Call API
#     latitude = 43.830802  # 吉林市的纬度，根据实际查询结果替换
#     longitude = 126.575303  # 吉林市的经度，根据实际查询结果替换
#     exclude_parts = 'current,minutely'  # 排除当前和每分钟预报，专注未来几天预报
#     url = f'https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude={exclude_parts}&appid={api_key}&units=metric&lang=zh_cn'

#     response = requests.get(url)
#     context = {}

#     if response.status_code == 200:
#         weather_data = response.json()
#         daily_forecast = weather_data['daily'][:5]  # 取前5天的预报
        
#         # 获取并格式化所需信息
#         context = {
#             'city': '吉林',
#             'forecasts': [
#                 {
#                     'date': datetime.utcfromtimestamp(day['dt']).strftime('%Y-%m-%d'),
#                     'temperature': {
#                         'day': day['temp']['day'],
#                         'night': day['temp']['night'],
#                     },
#                     'description': day['weather'][0]['description'],
#                     'humidity': day['humidity'],
#                     'pressure': day['pressure'],
#                     'wind_speed': day['wind_speed'],
#                     'sunrise': datetime.utcfromtimestamp(day['sunrise']).strftime('%H:%M'),
#                     'sunset': datetime.utcfromtimestamp(day['sunset']).strftime('%H:%M'),
#                     'data_time': datetime.utcfromtimestamp(weather_data['current']['dt']).strftime('%Y-%m-%d %H:%M:%S'),  # 当前数据时间
#                 } 
#                 for day in daily_forecast
#             ],
#         }
#     else:
#         context = {'error_message': '无法获取天气信息'}

#     return render(request, 'SmartCenter/trend.html', context)

def SmartCenter_user(request):
    context = {'title': 'My Page Title'}  # 数据字典
    # return render(request, '/templates/trend.html', context)  # 使用模板
    return render(request, 'SmartCenter/trendcopy.html', context)