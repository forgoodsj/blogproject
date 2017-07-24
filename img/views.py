# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Img
# Create your views here.

def showImg(request):
    imgs = Img.objects.all()
    return render(request, 'pic/index.html',{'imgs':imgs})