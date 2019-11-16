from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from . models import Send
from datetime import datetime
from login.models import User
from login.views import login
from login.views import register
import os
from .forms import UploadImageForm
from django.contrib.auth.mixins import LoginRequiredMixin
from comments.models import Comments


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


# 上传图片视图
def upload(request):
    if request.session.get('is_login', None):
        if request.method == 'GET':
            return redirect('index')
        elif request.method == 'POST':
            content_photo = request.FILES.get("upload", None)
            if not content_photo:
                return HttpResponse("没有上传内容!")
            position_name = os.path.join('E:\\site\\learn\\static\\photo')

            storage_location = open(position_name, 'wb+')
            for chunk in content_photo.chunks():
                storage_location.write(chunk)
            storage_location.close()
            return HttpResponse("上传成功!")
        else:
            return HttpResponseRedirect("不支持的请求方法!")
    else:
        return render(request, 'login/login.html')


# 修改用户头像视图
# class UploadImageView(LoginRequiredMixin, View):
def upload_photo(request):
    print('我在修改头像里...')
    image_form = UploadImageForm(request.POST, request.FILES, instance=request.session.user)
    if image_form.is_valid():
        image_form.save(commit=True)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'faile'})
        #image = image_form.cleaned_data["image"]
        #request.user.image = image
        #request.user.save()
        #return HttpResponse("{'status':'success'}", content_type='application/json')


