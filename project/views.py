from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from project.models import *
import datetime

"""
Class appelé sur les urls Project
"""


class DetailProject(DetailView):
    template_name = 'project/detail-project.html'
    model = Project
    context_object_name = "project"


class ListProject(ListView):
    template_name = 'project/list-project.html'
    model = Project
    context_object_name = "projects"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListProject, self).get_context_data(**kwargs)
        return context


class CreateProject(CreateView):
    model = Project
    fields = ['name', 'description', 'file', 'date_start', 'date_end', 'token']
    success_url = reverse_lazy('listProject')


class DeleteProject(DeleteView):
    template_name = 'delete.html'
    model = Team


class UpdateProject(UpdateView):
    pass


"""
Class appelé sur les urls Groups
"""


class DetailGroup(DetailView):
    template_name = 'team/detail-team.html'
    model = Team
    context_object_name = "group"


class ListGroup(ListView):
    template_name = 'team/list-team.html'
    model = Team
    context_object_name = "groups"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListGroup, self).get_context_data(**kwargs)
        return context


class CreateGroup(CreateView):
    model = Team
    fields = ['name', 'project', 'max_user', 'private', 'token_remain']
    success_url = reverse_lazy('listGroup')


class DeleteGroup(DeleteView):
    template_name = 'delete.html'
    model = Team


class UpdateGroup(UpdateView):
    pass
