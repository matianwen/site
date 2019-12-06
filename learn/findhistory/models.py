from django.db import models


# 挖掘附近历史模型
class Findnearhistory(models.Model):
    gender = (
        ('男', '男'),
        ('女', '女'),
    )
    username = models.CharField('作者', max_length=16)
    sex = models.CharField('性别', max_length=32, choices=gender, default='男')
    placename = models.CharField('地名', max_length=20)
    history = models.TextField('历史', null=True)
    timenow = models.DateTimeField(auto_now_add=True)
    see = models.IntegerField('浏览数', default=0)
    photo = models.FileField('图片', upload_to="headimages/%Y/%m/%d/", default=u"headimages/history.png", max_length=100)


    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-timenow']
        verbose_name = '挖掘历史'
        verbose_name_plural = '挖掘历史'
