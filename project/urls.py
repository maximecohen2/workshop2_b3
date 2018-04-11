from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from project.views import *

urlpatterns = [
    url(r'^delete$', login_required(DeleteProject.as_view()), name='delete'),
    url(r'^create$', login_required(CreateProject.as_view()), name='create'),
    url(r'^update$', login_required(UpdateProject.as_view()), name='update'),
    ]
