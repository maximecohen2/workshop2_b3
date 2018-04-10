from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView


def user(response):
    return render(response, 'layout.html')

class UserView(DetailView):
    def post_list():
        pass

