from django.contrib import admin
from .models import *


# admin.site.register(Comments)

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'content', 'pub_date', 'chats_user', 'content_type')
