from django.contrib.auth import authenticate, login, logout
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
        else:
            return render(request, self.template_name, {'error': 'Invalid username or password'})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return redirect(reverse('main:index_view'))
        else:
            return redirect(reverse('account:login_view'))

class RegisterView(View):
    template_name = 'account/sign_up.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('main:index_view'))
        return render(request, self.template_name, {})
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        name = request.POST.get('name')
        last_name = request.POST.get('last-name')

        if password1 != password2:
            raise ValidationError('passwords are not same')
        user = User.objects.create_user(first_name=name, email=email, password=password1, username=username, last_name=last_name)
        login(request, user)
        return redirect(reverse('main:index_view'))
