from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

class LoginView(View):
    template_name = 'account/sign_in.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('main:index_view'))
        return render(request, self.template_name, {})
