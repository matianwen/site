from django.shortcuts import render
from .models import Findnearhistory


# 导航栏发现视图
def find(request):
    context = {}
    context['findhistory'] = Findnearhistory.objects.all().order_by("-timenow")
    return render(request, 'find/find.html', context)


# 挖掘显示视图
def findsecondpage(request):
    context ={}
    return render(request, 'find/findsecondpage.html', context)


# 附近历史详情
def findnearhistory(request):
    context = {}
    return render(request, 'find/findnearhistory.html', context)
