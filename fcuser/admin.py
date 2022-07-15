from django.contrib import admin

# Register your models here.

from .models import Fcuser

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email', ) # 튜플형태로 만들어주기

admin.site.register(Fcuser, FcuserAdmin)