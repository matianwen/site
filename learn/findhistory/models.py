from django.db import models

# Create your models here.

# 挖掘附近历史模型
class Fundnearhistory(models.Model):
    username = models.CharField('作者', max_length=16)
    placename = models.CharField('地名', max_length=20)
    history = models.CharField('历史', max_length=200)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '挖掘历史'
        verbose_name_plural = '挖掘历史'

