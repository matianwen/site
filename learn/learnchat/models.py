from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from slugify import slugify
from django import forms
import login


# 标签模型
class Tags(models.Model):
    tagsname = models.CharField('标签名称', max_length=20, default='')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.tagsname


# 发布内容模型
class Send(models.Model):
    content = models.TextField('内容', null=True)   # 内容
    createTime = models.DateTimeField('发布日期', null=True)   # 时间
    # Temp = models.ForeignKey('login.User', verbose_name='作者', on_delete=models.CASCADE)   # 作者login.User
    Temp = models.CharField('作者', max_length=16)
    # tags = models.ManyToManyField(Tags, verbose_name='标签')
    see = models.IntegerField('浏览数', default=0)
    recommend = models.BooleanField('推荐言行', default=False)
    headphoto = models.FileField(upload_to="headimages/%Y/%m/%d/", default=u"headimages/default.png", max_length=100, verbose_name="头像")

    def __str__(self):
        return self.content

    def get_user(self):
        return self.Temp

    # 获取言行地址
    # def get_absolute_url(self):
        # return reverse('comments:commentviews', args=[self.id])

    class Meta:
        verbose_name = '发布内容'
        verbose_name_plural = '发布内容'


"""
# 用户信息模型
class Information(models.Model):
    user_name = models.ForeignKey('login.User', on_delete=models.CASCADE)
    chats_num = models.CharField('Send.content', max_length=100, unique=True)
    read_chat = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.chats_num

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
"""


# 用户更新头像模型
class Updateheadpoto(models.Model):
    username = models.CharField(max_length=16)
    avatar = models.FileField(upload_to="headimages/%Y/%m/%d/", default=u"headimages/default.png", max_length=100, verbose_name="头像")
    # avatar = models.ImageField(upload_to="headimages/%Y/%m/%d/", default=u"headimages/default.png", max_length=100, verbose_name="头像")
    # ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '更换头像'
        verbose_name_plural = '更换头像'




