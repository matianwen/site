from django.shortcuts import render, redirect, get_object_or_404, render_to_response, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from . models import Send
from datetime import datetime
from login.models import User
from login.views import login
from login.views import register
import os
from django.contrib.auth.mixins import LoginRequiredMixin
from comments.models import Comments
from .models import Updateheadpoto
import time
from login.models import Profile


# 发布内容视图
def send_content(request):
    if request.method == "GET":
        print('这个是GET请求...')
        return redirect("index")
    else:
        # 新建对象
        send_fb = Send()
        # 获取content内容
        send_fb.content = request.POST.get('content')
        print('获取发表内容:', send_fb.content)
        if send_fb.content == "":
            return redirect('index')

        # 获取当前时间
        send_fb.createTime = datetime.now()

        # 获取到用户的id
        user_id = request.session.get('user_name')
        print('用户名:', user_id)

        # 通过主键来获取login项目中的id
        # user_login = User.objects.get(name=user_id)
        # print('数据库用户名:', user_login)

        send_fb.Temp = user_id
        send_fb.save()
        print("发布成功...")
    return redirect('index')


# 用户信息设置视图
def user_info(request):
    context = {}
    context['userinfo'] = User.objects.all()
    context['headimge'] = Updateheadpoto.objects.all()
    context['introduceuser'] = Profile.objects.filter(user_id=request.session.get('user_id'))
    # context['usersex'] = User.objects.filter(sex=request.session.get('get_sex_display '))
    # context['loginip'] = request.META['HTTP_X_FORWARDED_FOR']
    return render(request, 'user/userinfo.html', context)


# 我的主页视图
def user_home(request):
    context = {}
    # select * from learnchat_send where Temp='陈建国';
    context['allcontent'] = Send.objects.all().order_by("-createTime")
    context['headimge'] = Updateheadpoto.objects.all()
    context['userintroduce'] = Profile.objects.filter(user_id=request.session.get('user_id'))
    # context['mycontentnum'] = Send.objects.filter(Temp=request.session.get('user_name')).order_by("-createTime")  # 查询某个用户发表的内容
    return render(request, 'user/userhome.html', context)


# 消息通知视图
def noticeinfo(request):
    context = {}
    # user = request.user
    # context['notifies'] = user.notifications.all()
    return render(request, 'user/noticeinfo.html', context)


# 黑洞视图
def blackhole(request):
    context = {}
    return render(request, 'user/blackhole.html', context)


# 上传头像视图
def updateheadphoto(request):
    context = {}
    print('我在修改头像里...')
    if request.method == "POST":
        name = request.session.get('user_name')
        # 上传新头像之前把旧的头像删除
        Updateheadpoto.objects.filter(username=name).delete()

        avatar = request.FILES.get('avatar')
        headpoto = Updateheadpoto.objects.create(username=name, avatar=avatar)
        headpoto.save()
        context['headpotoo'] = headpoto
        print('头像上传成功...')
    return render(request, 'user/updateheadphoto.html', context)


# 推荐详情视图
def recommenddetails(request):
    context = {}
    context['recommendteta'] = Send.objects.filter(recommend=1)
    context['recommendall'] = Send.objects.all()
    context['headpoto'] = Updateheadpoto.objects.all()
    return render(request, 'user/recommenddetails.html', context)


# 站内搜索视图
def searchall(request):
    context = {}
    get_input = request.GET.get('get_input')
    print('获取搜索关键字：', get_input)
    message = ''

    referer = request.META.get('HTTP_REFERER', reverse('index'))
    if not get_input:
        error_message = '请输入搜索关键字'
        return render(request, 'error.html', {'message': error_message , 'redirect_to': referer})

    # context['alldata'] = Send.objects.all().values("Temp","content")  #  获取所有的Temp,content数据，返回QuerySet，里面包含的是字典
    searchcontent = Send.objects.filter(content__icontains=get_input)  # exclude(body_text__icontains=get_input)
    searchatemp = Send.objects.filter(Temp__icontains=get_input)
    searchtime = Send.objects.filter(createTime__icontains=get_input)
    context['returnsearch'] = (searchcontent|searchatemp|searchtime).distinct()
    # context['userall'] = Send.objects.filter(Temp__icontains=get_input)

    return render(request, 'user/searchall.html', context)


