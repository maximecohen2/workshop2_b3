from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from project.views import *

urlpatterns = [
    # Url concernant la table Project
    url(r'^delete$', login_required(DeleteProject.as_view()), name='deleteProject'),
    url(r'^create$', login_required(CreateProject.as_view()), name='createProject'),
    url(r'^update$', login_required(UpdateProject.as_view()), name='updateProject'),
    url(r'^detail/(?P<pk>[0-9]+)$', login_required(DetailProject.as_view()), name='detailProject'),
    url(r'^$', login_required(ListProject.as_view()), name='listProject'),

    # Url concernant la table Group
    url(r'^group/delete$', login_required(DeleteGroup.as_view()), name='deleteGroup'),
    url(r'^group/create$', login_required(CreateGroup.as_view()), name='createGroup'),
    url(r'^group/update$', login_required(UpdateGroup.as_view()), name='updateGroup'),
    url(r'^group/detail/(?P<pk>[0-9]+)$', login_required(DetailGroup.as_view()), name='detailGroup'),
    url(r'^group/$', login_required(ListGroup.as_view()), name='listGroup'),
    ]
