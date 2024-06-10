from django.shortcuts import render
from django.views import View


class LoginView(View):

    def get(self, request):
        return render(request, 'account/sign_in.html', {})
