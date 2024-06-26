from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect, reverse
from django.shortcuts import render_to_response
from . models import *
import hashlib
from . models import User
from . import models
from . forms import UserForm, RegisterForm
from learnchat.models import Send
# from learnchat.models import Information
from django.db.models.aggregates import Count
from comments.models import Comments
from learnchat.models import Updateheadpoto
import time
from django.contrib.contenttypes.models import ContentType
from comments.forms import CommentForm
from likes.models import Likecount
from django.core.paginator import Paginator

learnchats_page_number = 10 # 每10条进行分页

# 主页视图
def index(request):
    contexts = {}
    # contexts['learnchats'] = Send.objects.all().order_by("-createTime")  # 显示所有发布内容视图

    chat_all_list = Send.objects.all().order_by("-createTime")
    paginator = Paginator(chat_all_list, learnchats_page_number)
    page_num = request.GET.get('page', 1) # 获取url的页面参数（GET请求）
    page_of_chat = paginator.get_page(page_num)
    currentr_page_num = page_of_chat.number # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + list(range(currentr_page_num, min(currentr_page_num + 2, paginator.num_pages) + 1))

    # 加上省略页码标记
    if page_range[0] -1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    contexts['learnchats'] = page_of_chat
    contexts['page_range'] = page_range

    contexts['recommendcontent'] = Send.objects.filter(recommend=1)  # 热点推荐视图
    contexts['userlearnnum'] = Send.objects.filter(Temp=request.session.get('user_name'))

    learnchat_content_type = ContentType.objects.get_for_model(Send)
    comments = Comments.objects.filter(content_type=learnchat_content_type)
    contexts['comments'] = comments

    # contexts['comments_count'] = Comments.objects.filter(content_type=learnchat_content_type).count()
    # contexts['comments'] = Comments.objects.all()
    #data = {}
    #data['content_type'] = learnchat_content_type.model
    #data['object_id'] = Send.objects.filter()
    #contexts['comment_form'] = CommentForm(initial=data)
    #comment_form = CommentForm(request.POST)
    #if comment_form.is_valid():
       # content_type = comment_form.cleaned_data['content_type']
        #object_id = comment_form.cleaned_data['object_id']
    #contexts['comment_form'] = comment_form

    contexts['headpoto'] = Updateheadpoto.objects.all()   #  filter(username=request.session.get('is_login'))
    contexts['likecount'] = Likecount.objects.all().count()
    # contexts['likedall'] = Likecount.objects.filter(object_id=request.session.get('object_id'))
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
                    time.sleep(1) # 延时一秒
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


# 重置密码视图
def resetpassword(request):
    contexts = {}
    referer = request.META.get('HTTP_REFERER', reverse('index'))
    # if not request.session.get('is_login', None):
        # return render(request, 'error.html', {'message': '忘记密码了吧,让你不记密码 :-)', 'redirect_to': referer})

    return render(request, 'login/resetpassword.html', contexts)


# 注册登录协议视图
def useragreement(request):
    contexts = {}
    return render(request, 'login/useragreement.html', contexts)


# 隐私协议视图
def privacyagreement(request):
    contexts = {}
    return render(request, 'login/privacyagreement.html', contexts)


# 关于视图
def about(request):
    contexts ={}
    return render(request, 'login/about.html', contexts)


