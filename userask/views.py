from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth import authenticate, login, logout
from django.http import *


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


class DetailUserAsk(LoginRequiredMixin, DetailView):
    template_name = "user/detail-user.html"

    def get_context_data(self, **kwargs):
        context = super(DetailUserAsk, self).get_context_data(**kwargs)
        return context

