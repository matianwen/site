from django.contrib import admin
from . import models
from .models import *

# admin.site.register(models.User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sex', 'time_now')

