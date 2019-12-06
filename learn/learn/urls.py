'''
author: matianwen
date: 2019-9-18
info: 这个是一个web网站，是一个以古诗词的方式来表达自己内心的想法，这是一个比较偏向有才华的用户，可以简单的说，用户就是现代版的诗人，
把你说的话以古文形式说出来，你说的话像诗一样美丽。
'''

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from login import views
from learnchat.views import send_content
import comments
from learnchat.views import user_info
from learnchat.views import user_home
from findhistory.views import fund
from learnchat.views import noticeinfo
from learnchat.views import blackhole
from learnchat.views import updateheadphoto
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic.base import RedirectView
from findhistory.views import fundsecondpage
from learnchat.views import recommenddetails


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^captcha', include('captcha.urls')),
    url(r'^fund/', fund),
    url(r'^send_content', send_content),
    path('', include('comments.urls')),
    url(r'^user_info/', user_info),
    url(r'^user_home/', user_home),
    url(r'^noticeinfo/', noticeinfo),
    url(r'^blackhole/', blackhole),
    url(r'^updateheadphoto/', updateheadphoto),
    re_path(r'^media/(.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/images/favicon.ico')),
    # url(r'^fundsecondpage/', fundsecondpage),
    url(r'^recommenddetails/', recommenddetails),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
