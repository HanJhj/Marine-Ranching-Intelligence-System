# learn/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainInformation, name='MainInformation'),  # 空路径（即/learn/）将会调用learn应用的index视图
]