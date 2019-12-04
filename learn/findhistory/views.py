from django.shortcuts import render


# 发现视图
def fund(request):
    context = {}
    return render(request, 'find/fund.html', context)


# 挖掘显示视图
def fundsecondpage(request):
    context ={}
    return render(request, 'user/fundsecondpage.html', context)
