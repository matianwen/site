from django.db import models
from learnchat.models import Send
from login.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# 评论模型
class Comments(models.Model):
    # content_type = models.ForeignKey(Send, verbose_name='言行', on_delete=models.CASCADE, related_name='comment')
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id') # 评论对象

    content = models.TextField('评论内容')
    pub_date = models.DateTimeField('评论时间', auto_now_add=True)
    chats_user = models.CharField('评论者', max_length=16)

    # chats_user = models.ForeignKey('login.User', verbose_name='评论作者', on_delete=models.CASCADE)
    # user_like = models.ManyToManyField(User, verbose_name='点赞者', related_name='comments_liked')

    def __str__(self):
        return self.content

    class Meta:
        ordering = ('pub_date',)
        verbose_name = '评论内容'
        verbose_name_plural = '评论内容'
        ordering = ['-pub_date']


