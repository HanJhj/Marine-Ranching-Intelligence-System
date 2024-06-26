
from django.shortcuts import render
from .models import HardwareInfo
from datetime import date
# Create your views here.

def DataCenter(request):

    latest_info = HardwareInfo.objects.filter(date=date.today()).first()
    
    context = {
        'latest_info': latest_info,
    }
    return render(request, 'DataCenter/NCDindex.html', context)


