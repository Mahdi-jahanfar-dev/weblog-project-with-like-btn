from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, View, ListView
from .models import Contact
from .forms import ContactForm
from blog.models import Post, Category
class IndexView(ListView):
    template_name = 'main/index.html'
    model = Post
    context_object_name = 'post'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ContactUserView(View):
    template_name = 'main/contactus.html'
    form_class = ContactForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
    def post(self, request, *args, **kwargs):
        user_name = request.POST.get('user-name')
        text = request.POST.get('user-text')
        last_name = request.POST.get('user-lastname')
        Contact.objects.create(name=user_name, message=text, last_name=last_name)
        return redirect(reverse('main:index_view'))

