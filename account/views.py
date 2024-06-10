from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

class LoginView(View):
    template_name = 'account/sign_in.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('main:index_view'))
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password, email=email)
        if user is not None:
            login(request, user)
            return redirect(reverse('main:index_view'))
        raise ValidationError('Invalid username or password or email')
