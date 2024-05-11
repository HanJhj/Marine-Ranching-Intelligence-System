# UnderWater/urls.py  
from django.urls import path  
from . import views  # 假设你的视图函数在 views.py 文件中  
  
urlpatterns = [  
    path('', views.UnderWater, name='UnderWater'),  # 空路径（即/learn/）将会调用learn应用的index视图 
    # ...  
]