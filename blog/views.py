from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator


class PostList(View):

    def get(self, request):

        firstpost = Post.objects.first()
        posts = Post.objects.all()[1:]

        paginator = Paginator(posts, 1)

        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        # есть ли другие страницы
        is_paginated = page.has_other_pages()
        # есть ли пред. стр
        if page.has_previous():
            prev_url = f'?page={page.previous_page_number()}'
        else:
            prev_url = ''
        # есть ли след. стр
        if page.has_next():
            next_url = f'?page={page.next_page_number()}'
        else:
            next_url = ''

        context = {
            'posts': posts,
            'firstpost': firstpost,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url,
        }
        return render(request, 'blog/index.html', context=context)


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_create_form.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST, request.FILES)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect('/')
        return render(request, 'blog/post_create_form.html', context={'form': bound_form})
