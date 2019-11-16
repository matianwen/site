from learnchat.models import Send
from .models import Comments
from datetime import datetime
from login.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse


# 评论视图
def commentviews(request):
    if request.method == "POST":
        print('我在评论视图里...')
        chats_user = request.session.get('user_name')
        content = request.POST.get('content', '')

        content_type = request.POST.get('content_type', '')
        object_id = request.POST.get('object_id', '')

        model_class = ContentType.objects.get(model=content_type).model_class()
        model_obj = model_class.objects.get(pk=object_id)

        comment = Comments()
        comment.chats_user = chats_user
        comment.content = content
        comment.content_object = model_obj
        comment.save()

        referer = request.META.get('HTTP_REFERER', reverse('index'))
        return redirect(referer)

        '''
        comment.chats_user = User.objects.get(id=request.session.get('user_id'))
        # print('评论用户:', comment.chats_user)
        comment.content = request.POST.get('content', '')
        # print('评论内容:', comment.content)
        content_type = request.POST.get('content_type', '')
        # print('内容类型:', content_type)

        # model_class = ContentType.objects.get(model=content_type).model_class()
        model_class = ContentType.objects.get(model=content_type).model_class()
        object_id = request.POST.get('object_id')
        # print('object_id值:', object_id)
        model_obj = model_class.objects.get(pk=object_id)
        comment.content_object = model_obj
        comment.save()

        referer = request.META.get('HTTP_REFERER', reverse('index'))
        return redirect(referer)
        '''
    else:
        print('这特么的是GET请求啊.............')

'''
def show_comments(request):
    contexts = {}
    contexts['comments'] = Comments.objects.all()
    return render(request, 'login/newcomment.html', contexts)
'''