from django.urls import reverse_lazy
from django.views.generic import *
from request.models import *


class DetailRequest(DetailView):
    template_name = 'request/request.html'
    model = Request
    context_object_name = "request"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DetailRequest, self).get_context_data(**kwargs)
        return context


class ListRequest(ListView):
    template_name = 'request/list-request.html'
    model = Request
    context_object_name = "requests"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListRequest, self).get_context_data(**kwargs)
        return context


class CreateRequest(CreateView):
    model = Request
    fields = ['title', 'type', 'date', 'team', 'intervenant', 'Statut']
    success_url = reverse_lazy('listRequest')
