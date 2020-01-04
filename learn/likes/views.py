"""
author: matianwen
date: 2020-01-04
info: 点赞功能相关视图
"""
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from .models import Likecount, Likerecord
from django.http import JsonResponse
from django.db.models import ObjectDoesNotExist


def ErrorResponse(code, message):
    data = {}
    data['status'] = 'ERROR'
    data['code'] = code
    data['message'] = message
    return JsonResponse(data)


def SuccessResponse(liked_num):
    data = {}
    data['status'] = 'SUCCESS'
    data['liked_num'] = liked_num
    return JsonResponse(data)


def like_change(request):
    if not request.session.get('is_login', None):
        return ErrorResponse(400, '你还没有登录!')

    # 获取数据
    user = request.session.get('user_name')
    content_type = request.GET.get('content_type')
    object_id = int(request.GET.get('object_id'))

    try:
        content_type = ContentType.objects.get(model=content_type)
        model_class = content_type.model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except ObjectDoesNotExist:
        return ErrorResponse(401, '对象不存在!')

    if request.GET.get('is_like') == 'true':
        # 点赞
        like_record, created = Likerecord.objects.get_or_create(content_type=content_type, object_id=object_id, user=user)
        if created:
            # 未点赞过，进行点赞
            like_count, created = Likecount.objects.get_or_create(content_type=content_type, object_id=object_id)
            like_count.liked_num += 1
            like_count.save()
            return SuccessResponse(like_count.liked_num)
        else:
            # 已点过，不可重复
            return ErrorResponse(402, '你已经点赞过!')
    else:
        # 取消点赞
        if Likerecord.objects.filter(content_type=content_type, object_id=object_id, user=user).exists():
            # 点赞过，取消点赞
            like_record = Likerecord.objects.get(content_type=content_type, object_id=object_id, user=user)
            like_record.delete()
            # 总点赞数减一
            like_count, created = Likecount.objects.get_or_create(content_type=content_type, object_id=object_id)
            if not created:
                like_count.liked_num -= 1
                like_count.save()
                return SuccessResponse(like_count.liked_num)
            else:
                return ErrorResponse(404, '数据错误!')
        else:
            return ErrorResponse(403, '你没有点赞过，不能取消点赞!')
