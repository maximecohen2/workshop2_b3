from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings


class LoginView(TemplateView):
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')

        return render(request, self.template_name)


class LogoutView(TemplateView):
    def get(self, request, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')
