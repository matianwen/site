from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from login.models import User


# 点赞统计
class Likecount(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    liked_num = models.IntegerField(default=0)

    def __str__(self):
        return self.liked_num

    class Meta:
        verbose_name = '点赞统计'
        verbose_name_plural = '点赞统计'


# 点赞记录
class Likerecord(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.CharField(max_length=16)  # models.ForeignKey(User, on_delete=models.CASCADE)
    liked_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = '点赞记录'
        verbose_name_plural = '点赞记录'

