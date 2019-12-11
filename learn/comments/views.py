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
        print('用户:', chats_user)
        content = request.POST.get('content','')
        print('评论:', content)
        comment_time = datetime.now()
        print('时间:', comment_time)

        try:
            content_type = request.POST.get('content_type','')
            print('内容类型:', content_type)
            object_id = int(request.POST.get('object_id',''))
            print('对象id:', object_id)
            model_class = ContentType.objects.get(model=content_type).model_class()
            print('model_class值是:', model_class)
            model_obj = model_class.objects.get(pk=object_id)
            print('评论对象:', model_obj)

        except:
            return render(request,'error.html',{'message':'评论的对象不存在...'})

        comment = Comments()
        comment.chats_user = chats_user
        comment.content = content
        comment.content_object = model_obj
        # comment = Comments.objects.create(content_type=model_obj,object_id=object_id,content=content,pub_date=comment_time,chats_user=chats_user)
        comment.save()

        referer = request.META.get('HTTP_REFERER', reverse('index'))
        return redirect(referer)
    # else:
        # print('这特么的是GET请求啊......')


def show_comments(request):
    contexts = {}
    contexts['comments'] = Comments.objects.all()
    return render(request, 'login/newcomment.html', contexts)
