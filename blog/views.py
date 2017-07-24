# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.db.models.aggregates import Count
from django.http import HttpResponse
from .models import Post, Category, Tag
from comments.forms import CommentForm
import markdown
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    paginator = Paginator(post_list,10)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    #如果 page 的值是一个整数，但是值太大了。例如总共只有 4 页，但用户请求第 10 页的数据，
    # 这时候 paginator.page 方法会抛出 EmptyPage 异常。这里处理这个异常的方式是：返回最后一页的数据给用户。
    category_list = Category.objects.annotate(num_posts=Count('post'))
    return render(request, 'blog/index.html', context={
        'post_list':post_list,
        'category_list':category_list,
        #这里 annotate 不仅从数据库获取了全部分类，相当于使用了 all 方法，它还帮我们为每一个分类添加了一个 num_posts 属性，
        # 其值为该分类下的文章数，这样我们在模板中就可以调用这个属性，
    })

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post':post,
        'form':form,
        'comment_list':comment_list
    }
    return render(request, 'blog/detail.html', context=context)

def archives(request,year,month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html',context={
        'post_list':post_list,})

def category(request,pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html',context={'post_list':post_list,})

def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入'
        return render(request, 'blog/index.html', {'error_msg':error_msg})

    post_list = Post.objects.filter(title__icontains=q)
    return render(request, 'blog/index.html', {'error_msg':error_msg,
                                                'post_list':post_list})

def qiubai(request):
    #c1=Category.objects.create(name='qiubai')
    #t1=Tag.objects.create(name='qiubai')
    PostObj = Post.objects.create(id='100',
                                 title='321',
                                  body='123',
                                  )
    return HttpResponse('yes')
