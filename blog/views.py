from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Post, Category

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class CategoryDetailView(ListView):
    model = Post
    template_name = 'main/index.html'
    context_object_name = 'post'
    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return super(CategoryDetailView, self).get_queryset().filter(category=category)
