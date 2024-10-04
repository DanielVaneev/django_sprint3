from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post, Category
from datetime import datetime


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        pub_date__lt=datetime.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[0:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    queryset_category = Category.objects.filter(
        slug__exact=category_slug,
        is_published__exact=True
    )
    print(queryset_category)
    category = get_object_or_404(
        queryset_category
    )
    post_list = Post.objects.filter(
        pub_date__lt=datetime.now(),
        is_published=True,
        category=category.pk
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    queryset_post = Post.objects.filter(
        pub_date__lt=datetime.now(),
        is_published__exact=True,
        category__is_published=True
    )
    post = get_object_or_404(
        queryset_post,
        pk=pk
    )
    context = {'post': post}
    return render(request, template, context)
