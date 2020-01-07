from django.contrib import admin
from .models import *


# admin.site.register(Findnearhistory)
@admin.register(Findnearhistory)
class FindnearhistoryAdmin(admin.ModelAdmin):
    list_display = ('placename', 'username', 'sex', 'history', 'timenow', 'see', 'photo')
