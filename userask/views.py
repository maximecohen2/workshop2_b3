from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import *
from django.contrib.auth import authenticate, login, logout
from django.http import *

from userask.models import UserAsk


class LoginUserAsk(TemplateView):
    template_name = "login.html"

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')

        return render(request, self.template_name)


class LogoutUserAsk(LoginRequiredMixin, TemplateView):

    def get(self, request, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')


class HomeUserAsk(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeUserAsk, self).get_context_data(**kwargs)
        context['page_title'] = "Accueil"
        return context


class ListUserAsk(LoginRequiredMixin, ListView):
    template_name = "user/list-user.html"


class ProfilUserAsk(LoginRequiredMixin, TemplateView):
    template_name = "user/detail-user.html"

    def get_context_data(self, **kwargs):
        context = super(ProfilUserAsk, self).get_context_data(**kwargs)
        context['user'] = User.objects.select_related('userask').get(pk=self.request.user.id)
        return context

