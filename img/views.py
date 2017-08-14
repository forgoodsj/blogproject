# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from img.models import Img,ImgTag
from blog.models import Post
from .forms import ImgForm
from django.http import HttpResponse
# Create your views here.

def showImg(request):
    imgs = Img.objects.all()
    return render(request, 'pic/index.html',{'imgs':imgs})


def upload(request):
    tags = ImgTag.objects.all()
    return render(request,'pic/upload.html',{'tags':tags})


def Done(request):

    if request.method == 'POST':
        new_img = Img(
            img=request.FILES['img'],
            tag=ImgTag.objects.get(pk=request.POST['tag']),
            title=request.POST['title'],
            description=request.POST['description'],

        )
        new_img.save()
        text = "上传成功"
    imgs = Img.objects.all()
    return render(request, 'pic/done.html',{'imgs':imgs})

def homePage(request):
    imgs = Img.objects.all()[::-1][0:8]
    blog = Post.objects.all().order_by('-created_time')[0:2]
    return render(request, 'pic/Homepage1.html',{'imgs':imgs,'blogs':blog})

