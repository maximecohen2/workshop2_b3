from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from request.views import *

urlpatterns = [
#    url(r'^delete$', login_required(DeleteProject.as_view()), name='deleteProject'),
#    url(r'^create$', login_required(CreateProject.as_view()), name='createProject'),
#    url(r'^update$', login_required(UpdateProject.as_view()), name='updateProject'),
    url(r'^detail/(?P<pk>[0-9]+)$', login_required(DetailRequest.as_view()), name='detailRequest'),
    url(r'^$', login_required(ListRequest.as_view()), name='listRequest'),
    ]