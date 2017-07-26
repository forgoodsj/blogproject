
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Img,Tag
# Register your models here.
class ImgAdmin(admin.ModelAdmin):
    list_display = ('img',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)



admin.site.register(Img,ImgAdmin)
admin.site.register(Tag,TagAdmin)