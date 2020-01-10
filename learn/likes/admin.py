from django.contrib import admin
from . models import *


@admin.register(Likecount)
class LikecountAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'liked_num', 'object_id', 'content_type')


@admin.register(Likerecord)
class LikerecordAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'object_id', 'user', 'liked_time', 'content_type')
