"""workshop2_b3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from userask.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # page admin de django
    path('admin/', admin.site.urls),

    # page du sites
    url(r'^$', HomeUserAsk.as_view(), name="home"),
    url(r'^home$', HomeUserAsk.as_view()),
    url(r'^connexion$', LoginUserAsk.as_view(), name="connexion"),
    url(r'^logout$', LogoutUserAsk.as_view(), name='logout'),
    url(r'^profil$', ProfilUserAsk.as_view(), name="profil"),
    url(r'^team$', login_required(TemplateView.as_view(template_name='team/detail-team.html'))),
    url(r'^project-list', login_required(TemplateView.as_view(template_name='project/list-project.html'))),
    url(r'^jetons-list', login_required(TemplateView.as_view(template_name='jetons-list.html'))),
    url(r'^project/', include('project.urls')),
]

