from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from django.shortcuts import render_to_response
from . models import *
import hashlib
from . models import User
from . import models
from . forms import UserForm, RegisterForm
from learnchat.models import Send
from learnchat.models import Information
from django.db.models.aggregates import Count
from comments.models import Comments


# 主页视图
def index(request):
    contexts = {}
    contexts['learnchats'] = Send.objects.all().order_by("-createTime")  # 显示所有发布内容视图
    contexts['recommendcontent'] = Send.objects.filter(recommend=1)  # 热点推荐视图
    contexts['comments'] = Comments.objects.all()
    return render(request, 'login/index.html', contexts)


# 登录视图
def login(request):
    if request.session.get('is_login', None):
        # return render(request, 'login/index.html')
        return redirect('index')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容!"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('index')
                else:
                    message = "密码不正确!"
            except:
                message = "用户名不存在!"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


# 注册视图
def register(request):
    if request.session.get('is_login', None):
        # return redirect("index")
        return render(request, 'login/index.html')
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容!"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = "两次输入的密码不同!"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '该用户已经存在，请重新选择用户!'
                    return render(request, 'login/register.html', locals())
                same_name_user = models.User.objects.filter(email=email)
                if same_name_user:
                    message = '该邮箱地址已被注册，请使用别的邮箱!'
                    return render(request, 'login/register.html', locals())

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


# 注销视图
def logout(request):
    if not request.session.get('is_login', None):
        return redirect('index')
        # return render(request, 'login/index.html')
    request.session.flush()
    return redirect('index')
    # return render(request, 'login/index.html', locals())


# 密码哈希加密视图
def hash_code(s, salt='login'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()




