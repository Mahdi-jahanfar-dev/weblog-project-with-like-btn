from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView

from .models import Post, Category, Comment

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    def post(self, request, *args, **kwargs):
        content = request.POST.get('content')
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        Comment.objects.create(post=post, content=content, author=self.request.user)
        return redirect('blog:blog_detail', slug=self.kwargs['slug'])


class CategoryDetailView(ListView):
    model = Post
    template_name = 'main/index.html'
    context_object_name = 'post'
    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return super(CategoryDetailView, self).get_queryset().filter(category=category)
