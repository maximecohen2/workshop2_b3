from django.shortcuts import render, get_object_or_404
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
    name = None
    description = None
    file = None
    date_start = datetime.datetime.now()
    date_end = date_start + datetime.timedelta(days=270)


class DeleteProject(DeleteView):
    template_name = 'delete.html'

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return render(self.request, self.template_name, {})


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
    template_name = 'team/detail-team.html'
    model = Team
    context_object_name = "groups"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListGroup, self).get_context_data(**kwargs)
        return context


class CreateGroup(CreateView):
    model = Team
    name = None
    project = None
    max_user = None
    private = None
    token_remain = None


class DeleteGroup(DeleteView):
    template_name = 'delete.html'

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return render(self.request, self.template_name, {})


class UpdateGroup(UpdateView):
    pass
