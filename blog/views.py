from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from .models import Post
from .forms import PostForm


class PostList(View):

    def get(self, request):
        posts = Post.objects.all()
        firstpost = Post.objects.first()
        context = {
            'posts': posts,
            'firstpost': firstpost,
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
            return redirect(new_post)
        return render(request, 'blog/post_create_form.html', context={'form': bound_form})
