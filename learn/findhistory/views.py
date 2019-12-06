from django.shortcuts import render
from .models import Findnearhistory


# 导航栏发现视图
def fund(request):
    context = {}
    context['findhistory'] = Findnearhistory.objects.all().order_by("-timenow")
    return render(request, 'find/fund.html', context)


# 挖掘显示视图
def fundsecondpage(request):
    context ={}
    return render(request, 'find/fundsecondpage.html', context)
