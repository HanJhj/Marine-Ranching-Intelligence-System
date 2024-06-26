# learn/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainInformation, name='MainInformation'),  
    path('MainInformation_user/', views.MainInformation_user, name='MainInformation_user'),
    path('upload', views.Upload, name='Upload'),
    path('on-off',views.on_off,name='on-off'),
]