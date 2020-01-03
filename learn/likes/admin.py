from django.contrib import admin
from . models import *


@admin.register(Likecount)
class LikecountAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'object_id', 'content_object', 'liked_num')


@admin.register(Likerecord)
class LikerecordAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'object_id', 'content_object', 'user', 'liked_time')
