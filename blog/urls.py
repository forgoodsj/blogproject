# -*- coding: utf-8 -*-
__author__ = 'jun'
from django.conf.urls import url

from . import views

app_name = 'blog'
#此外我们通过 app_name='blog' 告诉 Django 这个 urls.py 模块是属于 blog 应用的，这种技术叫做视图函数命名空间。
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category')
]
#绑定关系的写法是把网址和对应的处理函数作为参数传给 url 函数（第一个参数是网址，第二个参数是处理函数）
#另外我们还传递了另外一个参数 name，这个参数的值将作为处理函数 index 的别名，这在以后会用到。