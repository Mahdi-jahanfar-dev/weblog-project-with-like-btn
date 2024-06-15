from audioop import reverse

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, View

from .models import Post, Category, Comment, Like


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def post(self, request, *args, **kwargs):
        content = request.POST.get('content')
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(post=post, content=content, author=self.request.user, parent_id=parent_id)
        return redirect('blog:blog_detail', slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            if self.request.user.likes.filter(post__slug=self.object.slug, author_id=self.request.user.id).exists():
                context['likes'] = True
            else:
                context['likes'] = False
            return context
        else:
            context = super().get_context_data(**kwargs)
            context['likes'] = None
            return context


class CategoryDetailView(ListView):
    model = Post
    template_name = 'main/index.html'
    context_object_name = 'post'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return super(CategoryDetailView, self).get_queryset().filter(category=category)


class Like_view(View):
    # model = Post
    # template_name = 'blog/post_detail.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                like = Like.objects.get(post__slug=self.kwargs['slug'], author_id=self.request.user.id)
                like.delete()
                return JsonResponse({'response': 'unliked'})
            except:
                Like.objects.create(post_id=self.kwargs['pk'], author_id=self.request.user.id)
            return JsonResponse({'response': 'liked'})
        else:
            return redirect('account:login_view')