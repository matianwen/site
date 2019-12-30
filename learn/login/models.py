from django.db import models
from django import forms
#from django.contrib.auth.models import User #


# 用户模型
class User(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE) #
    gender = (
        ('男', '男'),
        ('女', '女'),
    )
    name = models.CharField('名字', max_length=128, unique=True)
    password = models.CharField('密码', max_length=256)
    email = models.EmailField('邮箱', unique=True)
    sex = models.CharField('性别', max_length=32, choices=gender, default='男')
    time_now = models.DateTimeField('注册时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-time_now']  # 元数据里定义用户按创建时间的反序排列，也就是最近的最先显示
        verbose_name = '用户'   # 自定义一个易于理解的名称,例如verbose_name = '地址', 用来标志这个表时用来存放地址信息的
        verbose_name_plural = '用户'  # 如果此项没有设置，Django 会使用 verbose_name + "s"来表示


