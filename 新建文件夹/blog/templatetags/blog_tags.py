# -*- coding: utf-8 -*-
__author__ = 'jun'
from ..models import Post, Category
from django import template

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):#最新文章
    return Post.objects.all().order_by('-created_time')[:num]


#这里我们首先导入 template 这个模块，然后实例化了一个 template.Library 类，
#并将函数 get_recent_posts 装饰为 register.simple_tag。
#这样就可以在模板中使用语法 {% get_recent_posts %} 调用这个函数了。


@register.simple_tag
def archives():#按月归档
    return Post.objects.dates('created_time', 'month', order='DESC')
#接受三个参数，创建时间，精度到月（返回不同列表，比如3月列表和2月列表），降序排列

@register.simple_tag
def get_categories():#分类
    return Category.objects.all()