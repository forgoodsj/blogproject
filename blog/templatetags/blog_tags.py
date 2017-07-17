# -*- coding: utf-8 -*-
from django import template

from ..models import Post, Category
from django.db.models.aggregates import Count

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post'))
    #这里 annotate 不仅从数据库获取了全部分类，相当于使用了 all 方法，
    #它还帮我们为每一个分类添加了一个 num_posts 属性，其值为该分类下的文章数，这样我们在模板中就可以调用这个属性





