# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField() #存储大段文本

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    #摘要，可以为空
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User)
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})
    #第一个参数告诉是blog应用中 name=detail的函数
    #reverse去解析函数对应的URL，正则表达部分会被后面传入的参数pk替换
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])