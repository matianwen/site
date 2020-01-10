from django.contrib import admin
from . models import *

# admin.site.register(Send)
@admin.register(Send)
class SendAdmin(admin.ModelAdmin):
    list_display = ('content', 'Temp', 'createTime', 'see', 'recommend')

admin.site.register(Tags)
# admin.site.register(Information)
# admin.site.register(Updateheadpoto)

@admin.register(Updateheadpoto)
class UpdateheadpotoAdmin(admin.ModelAdmin):
    list_display = ('username', 'avatar')
