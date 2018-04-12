from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from userask.views import *

urlpatterns = [
    #url(r'^delete$', login_required(DeleteProject.as_view()), name='deleteUser'),
    #url(r'^create$', login_required(CreateProject.as_view()), name='createUser'),
    url(r'^list/$', ListUserAsk.as_view(), name='listUser'),
    url(r'^detail/(?P<pk>[0-9]+)$', DetailUserAsk.as_view(), name='detailUser'),
    url(r'^$', ProfilUserAsk.as_view(), name='profilUser'),
    ]
