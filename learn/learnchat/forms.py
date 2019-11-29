'''
项目表单UploadImageForm
'''
from django import forms
from django.db import models
from .models import Updateheadpoto

# 表单
'''
class UserProfile(models.Model):
    image = models.ImageField(upload_to="images/%Y/%m", default=u"images/default.png", max_length=100)



class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Updateheadpoto
        fields = ["avatar"]
'''