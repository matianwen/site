from django.shortcuts import render, redirect, get_object_or_404, render_to_response, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from . models import Send
from datetime import datetime
from login.models import User
from login.views import login
from login.views import register
import os
# from .forms import UploadImageForm
from django.contrib.auth.mixins import LoginRequiredMixin
from comments.models import Comments
from .models import Updateheadpoto
import time


# 发布内容视图
def send_content(request):
    if request.method == "GET":
        print('这个是GET请求...')
        return redirect("index")
    else:
        send_fb = Send()  # 新建对象

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
        user_login = User.objects.get(name=user_id)
        print('数据库用户名:', user_login)

        send_fb.Temp = user_login
        send_fb.save()
        print("发布成功...")
    return redirect('index')


# 用户信息设置视图
def user_info(request):
    context = {}
    return render(request, 'user/userinfo.html', context)


# 我的主页视图
def user_home(request):
    context = {}
    return render(request, 'user/userhome.html', context)


# 发现视图
def fund(request):
    context = {}
    return render(request, 'user/fund.html', context)


# 消息通知视图
def noticeinfo(request):
    context = {}
    return render(request, 'user/noticeinfo.html', context)


# 黑洞视图
def blackhole(request):
    context = {}
    return render(request, 'user/blackhole.html', context)


# 修改用户头像视图
'''
def upload_photo(request):
    print('我在修改头像里...')
    if request.method == "POST":
        avatar = request.FILES.get('avatar')

        with open(avatar.name, 'wb') as f:
            for line in avatar:
                f.write(line)
        return HttpResponse('ok')
    return render(request, 'userinfo.html')
'''


# 上传头像视图
def updateheadphoto(request):
    context = {}
    print('我在修改头像里...')
    if request.method == "POST":
        name = request.session.get('user_name')
        avatar = request.FILES.get('avatar')
        headpoto = Updateheadpoto.objects.create(username=name, avatar=avatar)
        headpoto.save()
        context['headpoto'] = headpoto
        # context['imghref'] = Updateheadpoto.objects.filter(id=1)[0]
        # return render(request, 'login/showcontent.html', context)
        # return render(request, 'login/showcontent.html', context)
        print('头像上传成功...')
    return render(request, 'user/updateheadphoto.html', context)


# 显示头像视图
def showheadpoto(request):
    contexts = {}
    headpoto = Updateheadpoto.objects.all()
    id = headpoto.id
    username = headpoto.username
    avatar = headpoto.avatar
    contexts['newpoto'].append(id,username,avatar)
    return render(request, 'login/index.html', contexts)

