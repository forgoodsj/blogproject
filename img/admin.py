
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Img
# Register your models here.
class ImgAdmin(admin.ModelAdmin):
    list_display = ('img',)



admin.site.register(Img,ImgAdmin)
