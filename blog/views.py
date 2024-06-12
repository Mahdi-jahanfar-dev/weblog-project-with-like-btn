from django.shortcuts import render
from django.views.generic import DetailView

from .models import Post

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'