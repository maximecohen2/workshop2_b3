from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *
from project.models import Project
import datetime


class ListProject(ListView):
    template_name = 'project/list-project.html'
    model = Project
    context_object_name = "projects"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListProject, self).get_context_data(**kwargs)
        test = Project.objects.all()
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
