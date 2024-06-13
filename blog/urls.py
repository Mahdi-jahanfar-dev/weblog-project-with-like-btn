from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('cat/<slug:slug>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='blog_detail')
]