from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, View
from .models import Contact
from .forms import ContactForm
class IndexView(TemplateView):
    template_name = 'main/index.html'

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

