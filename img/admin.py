
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Img,ImgTag
# Register your models here.
'''
class ImgInline(admin.StackedInline):
    model = Img
'''
class ImgAdmin(admin.StackedInline):
    model = Img



class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)




admin.site.register(Img)
admin.site.register(ImgTag,TagAdmin)
