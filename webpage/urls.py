# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^vendedor$', views.perfil_vendedor, name='perfil_vendedor'),
    url(r'^producto$', views.gestion_producto, name='gestion_producto'),
]
