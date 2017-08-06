# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from img.models import Img,Tag
from blog.models import Post, Category, Tag
from .forms import ImgForm
from django.http import HttpResponse
# Create your views here.

def showImg(request):
    imgs = Img.objects.all()
    return render(request, 'pic/index.html',{'imgs':imgs})


def upload(request):
    tags = Tag.objects.all()
    return render(request,'pic/uploadpage.html',{'tags':tags})


def uploadImg(request):

    if request.method == 'POST':
        new_img = Img(
            img=request.FILES['img'],
            tag=Tag.objects.get(pk=request.POST['tag'])
        )

        new_img.save()
        text = "上传成功"
    imgs = Img.objects.all()
    return render(request, 'pic/done.html',{'imgs':imgs})

def homePage(request):
    imgs = Img.objects.all()[0:2]
    blog = Post.objects.all().order_by('-created_time')[0:2]
    return render(request, 'pic/Homepage.html',{'imgs':imgs,'blogs':blog})

