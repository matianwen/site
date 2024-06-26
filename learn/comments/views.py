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
from notifications.signals import notify
from django.utils.html import strip_tags
from likes.models import *


# 评论视图
def commentviews(request):
    if request.method == "POST":
        referer = request.META.get('HTTP_REFERER', reverse('index'))
        print('进入评论视图里...')
        if not request.session.get('is_login', None):
            return render(request, 'error.html', {'message': '用户未登录...', 'redirect_to': referer})

        chats_user = request.session.get('user_name')
        print('用户:', chats_user)

        content = request.POST.get('content','')
        print('评论:', content)
        if content == '':
            return render(request, 'error.html', {'message': '评论内容不能为空...', 'redirect_to': referer})

        comment_time = datetime.now()
        print('时间:', comment_time)

        try:
            content_type = request.POST.get('content_type','')
            # print('内容类型:', content_type)
            object_id = int(request.POST.get('object_id',''))
            # print('对象id:', object_id)
            model_class = ContentType.objects.get(model=content_type).model_class()
            # print('model_class值是:', model_class)
            model_obj = model_class.objects.get(pk=object_id)
            print('评论对象:', model_obj)
        except:
            return render(request, 'error.html', {'message':'评论的对象不存在...', 'redirect_to': referer})

        comment = Comments()
        comment.chats_user = chats_user
        comment.content = content
        comment.content_object = model_obj
        # comment = Comments.objects.create(content_type=model_obj,object_id=object_id,content=content,pub_date=comment_time,chats_user=chats_user)
        comment.save()

        # 发送站内消息
        """
        if content is None:
            # 回复
            pass
        else:
            # 评论
            recipient = comment.content_object.get_user()

        notify.send(chats_user, recipient=recipient, verb='You have a message', action_object=comment)
        """
        return redirect(referer)


def show_comments(request):
    contexts = {}
    learnchat_content_type = ContentType.objects.get_for_model(Send)
    comments = Comments.objects.filter(content_type=learnchat_content_type, object_id=Send.id)
    contexts['comments'] = comments

    likescount = Likecount.objects.filter(content_type=learnchat_content_type, object_id=Send.id)
    contexts['likescount'] = likescount
    # contexts['comments_count'] = Comments.objects.filter(content_type=learnchat_content_type).count()
    # contexts['comments'] = Comments.objects.all()
    # contexts['coments_all'] = Comments.objects.filter()
    return render(request, 'login/newcomment.html', contexts)
